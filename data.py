from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        con = sql.connect('database.db')
        msg=""
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            cur = con.cursor()
            print("Did this")
            cur.execute("INSERT INTO student (name,addr,city,pin) VALUES(?, ?, ?, ?)",(nm,addr,city,pin) )
            print("did this too")
            con.commit()
            print("Did this ttoooo")
            msg = "Record successfully added"
        except:
            print("Rolling back why ??")
            con.rollback()
            msg = "error in insert operation"

        finally:
            con.close()
            return render_template("result.html", msg=msg)


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from student")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)