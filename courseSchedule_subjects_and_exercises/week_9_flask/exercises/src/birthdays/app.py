import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # GET DATA FROM FORM
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # DATA VALIDATION
        if not name or not month or not day:
            # If any field is empty, it redirects back.
            return redirect("/")

        try:
            # Convert to integers and validate ranges.
            month = int(month)
            day = int(day)

            if month < 1 or month > 12:
                return redirect("/")
            if day < 1 or day > 31:
                return redirect("/")

        except ValueError:
            # If it's not a valid number, it redirects.
            return redirect("/")

        # INSERT INTO DATABASE
        db.execute(
            "INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)",
            name,
            month,
            day,
        )

        return redirect("/")

    else:
        # GET REQUEST - GET ALL THE BIRTHDAYS
        birthdays = db.execute("SELECT * FROM birthdays ORDER BY month, day")

        return render_template("index.html", birthdays=birthdays)


@app.route("/delete", methods=["POST"])
def delete():
    """Delete a birthday from the database"""
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM birthdays WHERE id = ?", id)
    return redirect("/")


# # app.py (birthdays) => native to Python (without the CS50 library):

# import os
# import sqlite3
# from flask import Flask, redirect, render_template, request

# # Configure application
# app = Flask(__name__)


# # Configure para conectar ao banco de dados SQLite
# def get_db_connection():
#     conn = sqlite3.connect("birthdays.db")
#     conn.row_factory = sqlite3.Row  # Para retornar dicionários
#     return conn


# @app.after_request
# def after_request(response):
#     """Ensure responses aren't cached"""
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     response.headers["Expires"] = 0
#     response.headers["Pragma"] = "no-cache"
#     return response


# @app.route("/", methods=["GET", "POST"])
# def index():
#     conn = get_db_connection()

#     if request.method == "POST":
#         # GET DATA FROM FORM
#         name = request.form.get("name")
#         month = request.form.get("month")
#         day = request.form.get("day")

#         # DATA VALIDATION
#         if not name or not month or not day:
#             conn.close()
#             return redirect("/")

#         try:
#             # Convert to integers and validate ranges.
#             month = int(month)
#             day = int(day)

#             if month < 1 or month > 12:
#                 conn.close()
#                 return redirect("/")
#             if day < 1 or day > 31:
#                 conn.close()
#                 return redirect("/")

#         except ValueError:
#             conn.close()
#             return redirect("/")

#         # INSERT INTO DATABASE
#         conn.execute(
#             "INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)",
#             (name, month, day),
#         )
#         conn.commit()
#         conn.close()

#         return redirect("/")

#     else:
#         # GET REQUEST - GET ALL THE BIRTHDAYS
#         birthdays = conn.execute(
#             "SELECT * FROM birthdays ORDER BY month, day"
#         ).fetchall()
#         conn.close()

#         return render_template("index.html", birthdays=birthdays)


# @app.route("/delete", methods=["POST"])
# def delete():
#     """Delete a birthday from the database"""
#     id = request.form.get("id")
#     if id:
#         conn = get_db_connection()
#         conn.execute("DELETE FROM birthdays WHERE id = ?", (id,))
#         conn.commit()
#         conn.close()
#     return redirect("/")


# if __name__ == "__main__":
#     app.run(debug=True)
