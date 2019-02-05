import os

from flask import Flask, render_template, session, request, redirect
from flask_socketio import SocketIO, send, emit, join_room, leave_room

from helpers import login_required

app = Flask(__name__)
app.config["SECRET_KEY"] = "my secret key"
socketio = SocketIO(app)

# Keep track of channels created (Check for channel name)
channelsCreated = []

# Keep track of users logged (Check for username)
usersLogged = []

@app.route("/")
@login_required
def index():

    return render_template("index.html", channels=channelsCreated)

@app.route("/signin", methods=['GET','POST'])
def signin():
    ''' Save the username on a Flask session 
    after the user submit the sign in form '''

    # Forget any username
    session.clear()

    username = request.form.get("username")
    
    if request.method == "POST":

        if username in usersLogged:
            return render_template("error.html", message="that username already exists!")                   
        
        usersLogged.append(username)

        session["username"] = username

        # Remember the user session on a cookie if the browser is closed.
        session.permanent = True

        return redirect("/")
    else:
        return render_template("signin.html")

@app.route("/logout/<username>", methods=['GET'])
def logout(username):
    """ Logout user deleting session and popping out of users connected."""

    # Delete cookie
    session.pop("username", None)

    # Remove from list
    try:
        usersLogged.remove(username)
    except ValueError:
        pass

    return redirect("/")

@app.route("/create", methods=['GET','POST'])
def create():

    # Get channel name from form
    newChannel = request.form.get("channel")

    if request.method == "POST":

        if newChannel in channelsCreated:
            return render_template("error.html", message="that channel already exists!")
        
        session["current_channel"] = newChannel

        # Add channel to global list of channels
        channelsCreated.append(newChannel)

        return redirect("/channels/" + newChannel)
    
    else:

        return render_template("create.html", channels = channelsCreated)

@app.route("/channels/<channel>", methods=['GET','POST'])
@login_required
def channel(channel):
    """ Show channel page to send and receive messages """

    if request.method == "POST":
        
        return redirect("/")
    else:
        return render_template("channel.html", channels= channelsCreated, users=usersLogged)

@socketio.on("joined", namespace='/')
def joined(message):
    """ Broadcast a message to anounce that a user has joined the channel """
    # TODO: Fix namespaces

    username = session['username']
    room = session["current_channel"]
    join_room(room)
    emit('status', {'msg': username + ' has entered the channel.'}, room=room)

@socketio.on("send message")
def send_msg(data):
    """ Receive message and broadcast to all the users connected """ 
    msg = data['data']
    emit("announce message", {"msg": msg}, broadcast=True)