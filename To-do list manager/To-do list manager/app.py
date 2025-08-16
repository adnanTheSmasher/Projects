import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///manager.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expired"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    if "user_id" not in session:
        return redirect("/login")
    tasks = db.execute("SELECT * FROM tasks WHERE user_id = ?", session["user_id"])
    return render_template("index.html", tasks=tasks)


@app.route("/login", methods=["GET", "POST"])
def login():

    """LOG USER IN"""

    #Forget any user id
    session.clear()



    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure username and password were submitted
        if not username or not password:
            return apology("must provide username and password", 403)

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", username
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        #remember the user
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
         return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmation")

        if not username:
            return apology("must provide username", 400)
        elif not password:
            return apology("must provide password", 400)
        elif password != confirm_password:
            return apology("passwords don't match", 400)

        hash_pw = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", username, hash_pw)
        except:
            return apology("USERNAME already EXIST", 400)

        return redirect("/login")

    else:
        return render_template("register.html")


@app.route("/add", methods=["POST"])
@login_required
def addTask():
    if "user_id" not in session:
        return redirect("/login")
    task = db.execute("INSERT INTO tasks(user_id, task) VALUES(?, ?)", session["user_id"], request.form.get("task"))
    return redirect("/")

@app.route("/delete/<int:task_id>")
@login_required
def deleteTask(task_id):
    if "user_id" not in session:
        return redirect("/login")
    task = db.execute("DELETE FROM tasks WHERE user_id = ? AND id = ?", session["user_id"], task_id)
    return redirect("/")

@app.route("/complete/<int:task_id>")
@login_required
def completeTask(task_id):
    if "user_id" not in session:
        return redirect("/login")
    db.execute("UPDATE tasks SET completed = 1 WHERE id = ? AND user_id = ?", task_id, session["user_id"])
    return redirect("/")
