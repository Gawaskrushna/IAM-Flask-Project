from flask import Flask, render_template, request, redirect, session, flash
import sqlite3, hashlib

app = Flask(__name__)
app.secret_key = "secret123"


# DATABASE CONNECTION
def connect_db():
    return sqlite3.connect("database.db")


# CREATE TABLE AND DEFAULT SUPERADMIN
def create_table():

    conn = connect_db()

    conn.execute('''
    CREATE TABLE IF NOT EXISTS users
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
    )
    ''')

    # CHECK SUPERADMIN EXISTS

    check = conn.execute(
        "SELECT * FROM users WHERE role='superadmin'"
    ).fetchone()

    if not check:

        password = hashlib.sha256(
            "super123".encode()).hexdigest()

        conn.execute(
            "INSERT INTO users(username,password,role) VALUES(?,?,?)",
            ("superadmin", password, "superadmin")
        )

        print("✅ SuperAdmin created")
        print("Username: superadmin")
        print("Password: super123")

    conn.commit()
    conn.close()


#  CALL FUNCTION 
create_table()



# HOME
@app.route("/")
def home():
    return redirect("/login")



# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = hashlib.sha256(
            request.form["password"].encode()).hexdigest()

        conn = connect_db()

        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)).fetchone()

        conn.close()

        if user:

            session["id"] = user[0]
            session["username"] = user[1]
            session["role"] = user[3]

            flash("Login Successful")

            if user[3] == "superadmin":
                return redirect("/superadmin")

            elif user[3] == "admin":
                return redirect("/admin")

            elif user[3] == "employee":
                return redirect("/employee")

            elif user[3] == "user":
                return redirect("/user")

        else:

            flash("Invalid Login")

    return render_template("login.html")



# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]

        password = hashlib.sha256(
            request.form["password"].encode()).hexdigest()

        role = request.form["role"]

        try:

            conn = connect_db()

            conn.execute(
                "INSERT INTO users(username,password,role) VALUES(?,?,?)",
                (username, password, role))

            conn.commit()

            flash("User Registered Successfully")

        except:

            flash("Username already exists")

        finally:

            conn.close()

        return redirect("/login")

    return render_template("register.html")



# SUPERADMIN DASHBOARD
@app.route("/superadmin")
def superadmin():

    if session.get("role") != "superadmin":
        return redirect("/login")

    conn = connect_db()

    users = conn.execute("SELECT * FROM users").fetchall()

    total = len(users)

    conn.close()

    return render_template("superadmin.html",
                           users=users,
                           total=total)



# ADMIN DASHBOARD
@app.route("/admin")
def admin():

    if session.get("role") not in ["admin", "superadmin"]:
        return redirect("/login")

    conn = connect_db()

    users = conn.execute("SELECT * FROM users").fetchall()

    total = len(users)

    conn.close()

    return render_template("admin.html",
                           users=users,
                           total=total)



# ADD USER
@app.route("/add_user", methods=["POST"])
def add_user():

    if session.get("role") not in ["admin", "superadmin"]:
        return redirect("/login")

    username = request.form["username"]

    password = hashlib.sha256(
        request.form["password"].encode()).hexdigest()

    role = request.form["role"]

    conn = connect_db()

    conn.execute(
        "INSERT INTO users(username,password,role) VALUES(?,?,?)",
        (username, password, role))

    conn.commit()

    conn.close()

    flash("User Added Successfully")

    if session["role"] == "superadmin":
        return redirect("/superadmin")
    else:
        return redirect("/admin")



# DELETE USER
@app.route("/delete/<int:id>")
def delete(id):

    if session.get("role") not in ["admin", "superadmin"]:
        return redirect("/login")

    conn = connect_db()

    conn.execute("DELETE FROM users WHERE id=?", (id,))

    conn.commit()

    conn.close()

    flash("User Deleted Successfully")

    if session["role"] == "superadmin":
        return redirect("/superadmin")
    else:
        return redirect("/admin")



# EMPLOYEE DASHBOARD
@app.route("/employee")
def employee():

    if session.get("role") != "employee":
        return redirect("/login")

    return render_template("employee.html")



# USER DASHBOARD
@app.route("/user")
def user():

    if session.get("role") != "user":
        return redirect("/login")

    return render_template("user.html")



# LOGOUT
@app.route("/logout")
def logout():

    session.clear()

    flash("Logged Out Successfully")

    return redirect("/login")



# RUN
app.run(debug=True)