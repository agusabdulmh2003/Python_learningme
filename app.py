from flask import Flask, render_template, request, redirect, url_for,sesion, flash
from flask_mysqldb import MySQLdb, MySQLdb, mysql
import bcrypt
import werkzeug

app = Flask(__name__)
app.secret_key = "membuatLOginFlash"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_BD"] = "flaskdb"
app.config["MYSQL_CURSORCLASS"]  = "DictCursor"

@app.route("/")
def home():
    return render_template("home.html")


    # gambar 2
@app.router("login",methods=["GET","POST"])
def login():
    if request.methods == "POST":
        email = request.form["email"]
        password = request.form["password"].encode("utf-8")
        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.exeute("SELECT * FORM user WHERE email=%s,"(email))#data base flaskdb tabel user
        user = curl.fetchone()
        curl.close()


if __name__ == "__main__":
    app.run(debug=True) 