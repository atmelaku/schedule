from flask import Blueprint, render_template, request, g, redirect, url_for

from . import db


bp = Blueprint("schedules", __name__)

@bp.route("/", methods=("GET", "POST"))
def index():
    return render_template("index.html")

@bp.route("/schedule", methods=("GET", "POST"))
def schedule():

    """View for home page which shows list of to-do items."""


    if request.method == "POST":
        years = request.form['years']
        months = request.form['months']
        days = request.form['days']
        date = request.form['date']
        shift = request.form['shift']
        description = request.form['description']
        cur = db.get_db().cursor()
        error = None


        if not years:
            error = "year is rquired"
        if not months:
            error = "month is rquired"
        if not days:
            error = "day is rquired"
        if not years:
            date = "date is rquired"
        if not years:
            shift = "shift is rquired"
        if not years:
            description = "description is rquired"

        if error is None:

            cur = db.get_db().cursor()


            cur.execute(
            "INSERT INTO schedule (years, months, days, date, shift, description, author_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (years, months, days, date, shift, description, g.user['id'])

            )


            g.db.commit()

    cur = db.get_db().cursor()
    cur.execute('SELECT * FROM schedule WHERE author_id = %s',
                (g.user['id'],))
    schedule = cur.fetchall()


    return render_template("schedule.html", schedule=schedule)

@bp.route('/<int:id>/delete_schedule', methods=('POST',))
def delete_schedule(id):
    cur = db.get_db().cursor()
    cur.execute('DELETE FROM schedule WHERE id = %s', (id,))
    g.db.commit()
    cur.close()
    return redirect(url_for('schedules.schedule'))

# @bp.route('/<int:id>/edit_schedule', methods=('GET', 'POST',))
# def edit_schedule(id):
#
#     cur = db.get_db().cursor()
#
#     cur.execute(
#     'SELECT years, months, days, date, shift, description  FROM schedule WHERE id = %s',
#         (id,)
#
#     )
#
#     schedules = cur.fetchone()
#
#
#
#     if request.method == "POST":
#
#         years = request.form.get('years')
#         months = request.form.get('months')
#         days = request.form.get('days')
#         date = request.form.get('date')
#         shift = request.form.get('shift')
#         description = request.form.get('description')
#
#
#
#
#
#         cur.execute(
#                 'UPDATE schedule SET years = %s, months = %s, days = %s, date = %s, shift = %s, description = %s'
#                 ' WHERE id = %s',
#                 (years, months, days, date, shift, description, id)
#         )
#         g.db.commit()
#
#         cur.close()
#         return redirect(url_for('schedules.schedule'))
#
#
#     return render_template("edit.html", schedule=schedule)
