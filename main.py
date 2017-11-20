from flask import Flask
import sqlite3 as sql

from flask import flash
from flask import url_for

from forms import LoginForm


from flask import render_template
from flask import request
from flask import session

# from flask.ext.security import Security, SQL

app = Flask(__name__)


app.secret_key='1022394208409128301480198094809238409328409'



counts=[1,1,1,1,1,1]    # Don't Change This !!!!

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('login.html', form=form)
        else:
            if form.data['name']=='admin' and form.data['password']=='root@123':
                return render_template('main.html')
            else:
                flash('Wrong username or password')
                return render_template('login.html',form=form)
    elif request.method == 'GET':
        return render_template('login.html', form=form)



@app.route('/dashboard')
def dashboard():
    return render_template('main.html')

# For chemical:
@app.route('/chemical')
def chemical():
    return render_template('chemical.html')


@app.route('/addchemical', methods=['POST', 'GET'])
def addchemical():
    global counts
    if request.method == 'POST':
        con = sql.connect('test.db')
        msg=""
        try:
            name = request.form['name']
            formula = request.form['formula']
            phase = request.form['phase']
            temp = request.form['temp']
            price = request.form['price']
            quantity = request.form['quantity']
            is_hazardous = request.form['hazardous']

            cur = con.cursor()
            print("Did this")
            cur.execute("INSERT INTO CHEMICAL (ITEM_ID,NAME,FORMULA,PHASE,TEMP, PRICE,QUANTITY,IS_HAZARDOUS) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",(counts[0],name,formula,phase,temp,price,quantity,is_hazardous) )

            print("did this too")
            con.commit()
            print("Did this ttoooo")
            msg = "Record successfully added"
            counts[0]+=1
        except:
            print("Rolling back why ??")
            con.rollback()
            msg = "error in insert operation"

        finally:
            con.close()
            return render_template('main.html')

@app.route('/listchemical')
def listchemical():
    con = sql.connect("test.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from CHEMICAL")

    rows = cur.fetchall()
    return render_template('list.html',rows=rows)



# For non glassware:

@app.route('/nonglassware')
def nonglassware():
    return render_template('nonglassware.html')

@app.route('/addnonglassware', methods=['POST', 'GET'])
def addnonglassware():
    global counts
    if request.method == 'POST':
        con = sql.connect('test.db')
        msg=""
        try:
            name = request.form['name']
            price = request.form['price']
            quantity = request.form['quantity']

            cur = con.cursor()
            print("Did this")
            cur.execute("INSERT INTO NONGLASSWARE (ITEM_ID,NAME,PRICE,QUANTITY) VALUES(?, ?, ?, ?)",(counts[1],name,price,quantity) )

            print("did this too")
            con.commit()
            print("Did this ttoooo")
            msg = "Record successfully added"
            counts[1]+=1
        except:
            print("Rolling back why ??")
            con.rollback()
            msg = "error in insert operation"

        finally:
            con.close()
            return render_template("main.html")

@app.route('/listnonglassware')
def listnonglassware():
    con = sql.connect("test.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from NONGLASSWARE")

    rows = cur.fetchall()
    return render_template('listnonglassware.html',rows=rows)



# GLASSWARE:

@app.route('/glassware')
def glassware():
    return render_template('glassware.html')

@app.route('/addglassware', methods=['POST', 'GET'])
def addglassware():
    global counts
    if request.method == 'POST':
        con = sql.connect('test.db')
        msg=""
        try:
            name = request.form['name']
            capacity= request.form['capacity']
            price = request.form['price']
            quantity = request.form['quantity']

            cur = con.cursor()
            print("Did this")
            cur.execute("INSERT INTO GLASSWARE (ITEM_ID,NAME,CAPACITY,PRICE,QUANTITY) VALUES(?, ?, ?, ?, ?)",(counts[2],name,capacity,price,quantity) )

            print("did this too")
            con.commit()
            print("Did this ttoooo")
            msg = "Record successfully added"
            counts[2]+=1
        except:
            print("Rolling back why ??")
            con.rollback()
            msg = "error in insert operation"

        finally:
            con.close()
            return render_template("main.html")

@app.route('/listglassware')
def listglassware():
    con = sql.connect("test.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from GLASSWARE")

    rows = cur.fetchall()
    return render_template('listglassware.html',rows=rows)


# EXPERIMENT:

@app.route('/experiment')
def experiment():
    return render_template('experiment.html')

@app.route('/addexperiment', methods=['POST', 'GET'])
def addexperiment():
    global counts
    if request.method == 'POST':
        con = sql.connect('test.db')
        msg=""
        try:
            name = request.form['name']
            brief = request.form['brief']

            cur = con.cursor()
            print("Did this")
            cur.execute("INSERT INTO EXPERIMENT (ITEM_ID,NAME,BRIEF) VALUES(?, ?, ?)",(counts[3],name,brief) )

            print("did this too")
            con.commit()
            print("Did this ttoooo")
            msg = "Record successfully added"
            counts[3]+=1
        except:
            print("Rolling back why ??")
            con.rollback()
            msg = "error in insert operation"

        finally:
            con.close()
            return render_template("main.html")

@app.route('/listexperiment')
def listexperiment():
    con = sql.connect("test.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from EXPERIMENT")

    rows = cur.fetchall()
    return render_template('listexperiment.html',rows=rows)



# Final log table:

@app.route('/log')
def log():
    return render_template('log.html')

@app.route('/addlog', methods=['POST', 'GET'])
def addlog():
    global counts
    if request.method == 'POST':
        con = sql.connect('test.db')
        msg=""
        try:
            log_for = request.form['log_for']
            type = request.form['type']
            time = request.form['time']
            author = request.form['author']

            cur = con.cursor()
            print("Did this")
            cur.execute("INSERT INTO LOG (ITEM_ID,LOG_FOR,TYPE,TIME,AUTHOR) VALUES(?, ?, ?, ?, ?)",(counts[4],log_for,type,time,author) )

            print("did this too")
            con.commit()
            print("Did this ttoooo")
            msg = "Record successfully added"
            counts[4]+=1
        except:
            print("Rolling back why ??")
            con.rollback()
            msg = "error in insert operation"

        finally:
            con.close()
            return render_template("main.html")

@app.route('/listlog')
def listlog():
    con = sql.connect("test.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from LOG")

    rows = cur.fetchall()
    return render_template('listlog.html',rows=rows)



if __name__=='__main__':
    app.run(debug=True)
