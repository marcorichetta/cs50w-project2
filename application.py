import os

from flask import Flask, render_template, session, request, redirect
from flask_socketio import SocketIO, emit

from helpers import login_required

app = Flask(__name__)
app.config["SECRET_KEY"] = "my secret key"
socketio = SocketIO(app)

# Keep track of channels created
channelsCreated = []

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
        
        session["username"] = username

        # Remember the user session on a cookie if the browser is closed.
        session.permanent = True

        return redirect("/")
    else:
        return render_template("signin.html")

@app.route("/create", methods=['POST'])
def create():

    if request.method == "POST":

        session["variable"] = request.form.get("channel")

        channelsCreated.append(request.form.get("channel"))

        return render_template("index.html", channels = channelsCreated)