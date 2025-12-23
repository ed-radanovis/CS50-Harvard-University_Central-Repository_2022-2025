import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]

    # Get user's cash balance
    user = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = user[0]["cash"]

    # Get user's stocks from transactions
    stocks = db.execute(
        """
        SELECT symbol, SUM(shares) as total_shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING total_shares > 0
    """,
        user_id,
    )

    # Calculate current prices and totals
    portfolio = []
    total_value = cash

    for stock in stocks:
        quote = lookup(stock["symbol"])
        if quote:
            stock_value = quote["price"] * stock["total_shares"]
            portfolio.append(
                {
                    "symbol": stock["symbol"],
                    "name": quote["name"],
                    "total_shares": stock["total_shares"],
                    "price": quote["price"],
                    "total_value": stock_value,
                }
            )
            total_value += stock_value

    return render_template("index.html", stocks=portfolio, cash=cash, total=total_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide symbol", 400)

        if not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("must provide positive integer number of shares", 400)

        shares = int(shares)
        stock = lookup(symbol)

        if not stock:
            return apology("invalid symbol", 400)

        user_id = session["user_id"]
        user = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = user[0]["cash"]
        total_cost = stock["price"] * shares

        if cash < total_cost:
            return apology("can't afford", 400)

        # Update user's cash
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, user_id)

        # Record transaction
        db.execute(
            """
            INSERT INTO transactions (user_id, symbol, shares, price, type)
            VALUES (?, ?, ?, ?, 'buy')
        """,
            user_id,
            symbol.upper(),
            shares,
            stock["price"],
        )

        flash("Bought!")
        return redirect("/")

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions = db.execute(
        "SELECT * FROM transactions WHERE user_id = ? ORDER BY transacted DESC", user_id
    )
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        symbol = request.form.get("symbol")

        # Ensure symbol was submitted
        if not symbol:
            return apology("must provide symbol", 400)

        # Look up the stock symbol
        stock = lookup(symbol)

        # Ensure symbol is valid
        if stock is None:
            return apology("invalid symbol", 400)

        # Render the quoted template with stock info
        return render_template("quoted.html", stock=stock)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Get form inputs
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)

        # Ensure confirmation was submitted
        elif not confirmation:
            return apology("must confirm password", 400)

        # Ensure passwords match
        elif password != confirmation:
            return apology("passwords do not match", 400)

        # Check if username already exists BEFORE attempting insert
        existing_user = db.execute("SELECT id FROM users WHERE username = ?", username)
        if existing_user:
            # Username already exists - return apology
            return apology("username already exists", 400)

        # Hash the password
        hash_password = generate_password_hash(password)

        # Insert new user into database
        # Using try/except as a safety net, but primary check is above
        try:
            new_user_id = db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)",
                username,
                hash_password,
            )
        except ValueError:
            # This should rarely happen due to our check above, but handle it
            return apology("username already exists", 400)

        # Log the user in automatically
        session["user_id"] = new_user_id

        # Flash a success message
        flash("Registered successfully!")

        # Redirect user to home page - this should eventually return 200
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must select a stock", 400)

        if not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("must provide positive integer number of shares", 400)

        shares = int(shares)
        user_id = session["user_id"]

        # Check if user owns enough shares
        owned = db.execute(
            """
            SELECT SUM(shares) as total
            FROM transactions
            WHERE user_id = ? AND symbol = ?
        """,
            user_id,
            symbol.upper(),
        )

        total_owned = owned[0]["total"] if owned and owned[0]["total"] else 0

        if total_owned < shares:
            return apology("not enough shares", 400)

        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol", 400)

        total_value = stock["price"] * shares

        # Update user's cash
        db.execute(
            "UPDATE users SET cash = cash + ? WHERE id = ?", total_value, user_id
        )

        # Record transaction (negative shares for selling)
        db.execute(
            """
            INSERT INTO transactions (user_id, symbol, shares, price, type)
            VALUES (?, ?, ?, ?, 'sell')
        """,
            user_id,
            symbol.upper(),
            -shares,
            stock["price"],
        )

        flash("Sold!")
        return redirect("/")

    # GET request - show sell form
    user_id = session["user_id"]

    # Get stocks the user owns
    stocks = db.execute(
        """
        SELECT symbol
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING SUM(shares) > 0
    """,
        user_id,
    )

    return render_template("sell.html", stocks=stocks)


# # app.py (finance) => native to Python (without the CS50 library):

# import os
# import sqlite3
# from flask import Flask, flash, redirect, render_template, request, session, g
# from flask_session import Session
# from werkzeug.security import check_password_hash, generate_password_hash

# from helpers import apology, login_required, lookup, usd

# # Configure application
# app = Flask(__name__)

# # Custom filter
# app.jinja_env.filters["usd"] = usd

# # Configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)


# # Database connection
# def get_db():
#     """Get database connection"""
#     if "db" not in g:
#         g.db = sqlite3.connect("finance.db", check_same_thread=False)
#         g.db.row_factory = sqlite3.Row  # Para retornar dicionários
#     return g.db


# @app.teardown_appcontext
# def close_db(error):
#     """Close database connection"""
#     if "db" in g:
#         g.db.close()


# def db_execute(query, *args, fetch=False):
#     """Execute SQL query with similar behavior to cs50.SQL.execute()"""
#     conn = get_db()
#     cursor = conn.cursor()

#     try:
#         cursor.execute(query, args)

#         if query.strip().upper().startswith("SELECT"):
#             if fetch:
#                 result = cursor.fetchall()
#                 return [dict(row) for row in result]
#             else:
#                 result = cursor.fetchone()
#                 return dict(result) if result else None
#         elif query.strip().upper().startswith("INSERT"):
#             conn.commit()
#             return cursor.lastrowid
#         else:  # UPDATE, DELETE
#             conn.commit()
#             return cursor.rowcount
#     except sqlite3.IntegrityError:
#         conn.rollback()
#         raise ValueError("Integrity error (duplicate username)")
#     except Exception as e:
#         conn.rollback()
#         raise e


# @app.after_request
# def after_request(response):
#     """Ensure responses aren't cached"""
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     response.headers["Expires"] = 0
#     response.headers["Pragma"] = "no-cache"
#     return response


# @app.route("/")
# @login_required
# def index():
#     """Show portfolio of stocks"""
#     user_id = session["user_id"]

#     # Get user's cash balance
#     user = db_execute("SELECT cash FROM users WHERE id = ?", user_id)
#     cash = user["cash"] if user else 0

#     # Get user's stocks from transactions
#     stocks = db_execute(
#         """
#         SELECT symbol, SUM(shares) as total_shares
#         FROM transactions
#         WHERE user_id = ?
#         GROUP BY symbol
#         HAVING total_shares > 0
#     """,
#         user_id,
#         fetch=True,
#     )

#     # Calculate current prices and totals
#     portfolio = []
#     total_value = cash

#     for stock in stocks:
#         quote = lookup(stock["symbol"])
#         if quote:
#             stock_value = quote["price"] * stock["total_shares"]
#             portfolio.append(
#                 {
#                     "symbol": stock["symbol"],
#                     "name": quote["name"],
#                     "total_shares": stock["total_shares"],
#                     "price": quote["price"],
#                     "total_value": stock_value,
#                 }
#             )
#             total_value += stock_value

#     return render_template("index.html", stocks=portfolio, cash=cash, total=total_value)


# @app.route("/buy", methods=["GET", "POST"])
# @login_required
# def buy():
#     """Buy shares of stock"""
#     if request.method == "POST":
#         symbol = request.form.get("symbol")
#         shares = request.form.get("shares")

#         if not symbol:
#             return apology("must provide symbol", 400)

#         if not shares or not shares.isdigit() or int(shares) <= 0:
#             return apology("must provide positive integer number of shares", 400)

#         shares = int(shares)
#         stock = lookup(symbol)

#         if not stock:
#             return apology("invalid symbol", 400)

#         user_id = session["user_id"]
#         user = db_execute("SELECT cash FROM users WHERE id = ?", user_id)
#         cash = user["cash"]
#         total_cost = stock["price"] * shares

#         if cash < total_cost:
#             return apology("can't afford", 400)

#         # Update user's cash
#         db_execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, user_id)

#         # Record transaction
#         db_execute(
#             """
#             INSERT INTO transactions (user_id, symbol, shares, price, type)
#             VALUES (?, ?, ?, ?, 'buy')
#         """,
#             user_id,
#             symbol.upper(),
#             shares,
#             stock["price"],
#         )

#         flash("Bought!")
#         return redirect("/")

#     return render_template("buy.html")


# @app.route("/history")
# @login_required
# def history():
#     """Show history of transactions"""
#     user_id = session["user_id"]
#     transactions = db_execute(
#         "SELECT * FROM transactions WHERE user_id = ? ORDER BY transacted DESC",
#         user_id,
#         fetch=True,
#     )
#     return render_template("history.html", transactions=transactions)


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     """Log user in"""

#     # Forget any user_id
#     session.clear()

#     # User reached route via POST (as by submitting a form via POST)
#     if request.method == "POST":
#         # Ensure username was submitted
#         if not request.form.get("username"):
#             return apology("must provide username", 403)

#         # Ensure password was submitted
#         elif not request.form.get("password"):
#             return apology("must provide password", 403)

#         # Query database for username
#         rows = db_execute(
#             "SELECT * FROM users WHERE username = ?",
#             request.form.get("username"),
#             fetch=True,
#         )

#         # Ensure username exists and password is correct
#         if len(rows) != 1 or not check_password_hash(
#             rows[0]["hash"], request.form.get("password")
#         ):
#             return apology("invalid username and/or password", 403)

#         # Remember which user has logged in
#         session["user_id"] = rows[0]["id"]

#         # Redirect user to home page
#         return redirect("/")

#     # User reached route via GET (as by clicking a link or via redirect)
#     else:
#         return render_template("login.html")


# @app.route("/logout")
# def logout():
#     """Log user out"""

#     # Forget any user_id
#     session.clear()

#     # Redirect user to login form
#     return redirect("/")


# @app.route("/quote", methods=["GET", "POST"])
# @login_required
# def quote():
#     """Get stock quote."""

#     # User reached route via POST (as by submitting a form via POST)
#     if request.method == "POST":
#         symbol = request.form.get("symbol")

#         # Ensure symbol was submitted
#         if not symbol:
#             return apology("must provide symbol", 400)

#         # Look up the stock symbol
#         stock = lookup(symbol)

#         # Ensure symbol is valid
#         if stock is None:
#             return apology("invalid symbol", 400)

#         # Render the quoted template with stock info
#         return render_template("quoted.html", stock=stock)

#     # User reached route via GET (as by clicking a link or via redirect)
#     else:
#         return render_template("quote.html")


# @app.route("/register", methods=["GET", "POST"])
# def register():
#     """Register user"""

#     # User reached route via POST (as by submitting a form via POST)
#     if request.method == "POST":

#         # Get form inputs
#         username = request.form.get("username")
#         password = request.form.get("password")
#         confirmation = request.form.get("confirmation")

#         # Ensure username was submitted
#         if not username:
#             return apology("must provide username", 400)

#         # Ensure password was submitted
#         elif not password:
#             return apology("must provide password", 400)

#         # Ensure confirmation was submitted
#         elif not confirmation:
#             return apology("must confirm password", 400)

#         # Ensure passwords match
#         elif password != confirmation:
#             return apology("passwords do not match", 400)

#         # Check if username already exists BEFORE attempting insert
#         existing_user = db_execute(
#             "SELECT id FROM users WHERE username = ?", username, fetch=True
#         )
#         if existing_user:
#             # Username already exists - return apology
#             return apology("username already exists", 400)

#         # Hash the password
#         hash_password = generate_password_hash(password)

#         # Insert new user into database
#         try:
#             new_user_id = db_execute(
#                 "INSERT INTO users (username, hash) VALUES (?, ?)",
#                 username,
#                 hash_password,
#             )
#         except ValueError:
#             # This should rarely happen due to our check above, but handle it
#             return apology("username already exists", 400)

#         # Log the user in automatically
#         session["user_id"] = new_user_id

#         # Flash a success message
#         flash("Registered successfully!")

#         # Redirect user to home page
#         return redirect("/")

#     # User reached route via GET (as by clicking a link or via redirect)
#     else:
#         return render_template("register.html")


# @app.route("/sell", methods=["GET", "POST"])
# @login_required
# def sell():
#     """Sell shares of stock"""
#     if request.method == "POST":
#         symbol = request.form.get("symbol")
#         shares = request.form.get("shares")

#         if not symbol:
#             return apology("must select a stock", 400)

#         if not shares or not shares.isdigit() or int(shares) <= 0:
#             return apology("must provide positive integer number of shares", 400)

#         shares = int(shares)
#         user_id = session["user_id"]

#         # Check if user owns enough shares
#         owned = db_execute(
#             """
#             SELECT SUM(shares) as total
#             FROM transactions
#             WHERE user_id = ? AND symbol = ?
#         """,
#             user_id,
#             symbol.upper(),
#             fetch=True,
#         )

#         total_owned = owned[0]["total"] if owned and owned[0]["total"] else 0

#         if total_owned < shares:
#             return apology("not enough shares", 400)

#         stock = lookup(symbol)
#         if not stock:
#             return apology("invalid symbol", 400)

#         total_value = stock["price"] * shares

#         # Update user's cash
#         db_execute(
#             "UPDATE users SET cash = cash + ? WHERE id = ?", total_value, user_id
#         )

#         # Record transaction (negative shares for selling)
#         db_execute(
#             """
#             INSERT INTO transactions (user_id, symbol, shares, price, type)
#             VALUES (?, ?, ?, ?, 'sell')
#         """,
#             user_id,
#             symbol.upper(),
#             -shares,
#             stock["price"],
#         )

#         flash("Sold!")
#         return redirect("/")

#     # GET request - show sell form
#     user_id = session["user_id"]

#     # Get stocks the user owns
#     stocks = db_execute(
#         """
#         SELECT symbol
#         FROM transactions
#         WHERE user_id = ?
#         GROUP BY symbol
#         HAVING SUM(shares) > 0
#     """,
#         user_id,
#         fetch=True,
#     )

#     return render_template("sell.html", stocks=stocks)


# if __name__ == "__main__":
#     app.run(debug=True)
