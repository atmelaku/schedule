from flask import Flask, Blueprint, request, redirect, url_for, session, render_template, g, flash
from werkzeug.security import check_password_hash, generate_password_hash
from . import db

# import datetime
# import flask
# import flask_login
import functools

bp = Blueprint('auth', __name__,)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # getting the database
        cur = db.get_db().cursor()
        # define error variables

        error = None


        if not username:
            error = "Username is requerd!"
        elif not password:
            error = "password is required!"
        elif error is None:
            cur.execute(
                'SELECT id FROM users WHERE username = %s', (username,)
            )
            user = cur.fetchall()
            if user != []:
                error = "already in use"

        if error is None:
            cur.execute(
            "INSERT INTO users (username, password) VAlUES (%s, %s)",
            (username, generate_password_hash(password))

            )

            g.db.commit()


            return redirect(url_for("auth.login"))


    return render_template("register.html")

@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        cur = db.get_db().cursor()
        error = None
        cur.execute(
        "SELECT * FROM users WHERE username = %s", (username,)

        )
        user = cur.fetchone()
        cur.close()

        if user is None:
            error = "Incorrect username"
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password"

        if error is None:

            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("schedules.schedule"))

        flash(error)

    return (render_template("login.html"))
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    cur = db.get_db().cursor()
    if user_id is None:
        g.user = None
    else:
        cur.execute(
            'SELECT * FROM users WHERE id = %s', (user_id,)
        )
        g.user = cur.fetchone()
        cur.close()
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('schedules.index'))
