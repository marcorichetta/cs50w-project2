import os

from flask import Flask, render_template, session, request, redirect
from flask_socketio import SocketIO, emit

from helpers import login_required

app = Flask(__name__)
app.config["SECRET_KEY"] = "my secret key"
socketio = SocketIO(app)

# Keep track of channels created
channelsCreated = []
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
        return render_template("channel.html", channels= channelsCreated)

@socketio.on("send message")
def send(data):
    """ Receive message and broadcast to all the users connected """ 
    # TODO: Socketio rooms
    msg = data['data']
    emit("announce message", {"msg": msg}, broadcast=True)
