# from flask import Flask , redirect , url_for
# from flask import flash
# from flask import render_template
# from flask import request
# from flask import session

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'


# -----
# Helpers:
# @app.route('/index/<int:postID>')
# def show(postID):
#     return "You Entered %d" % postID
#
#
# @app.route('/index/<float:revNo>')
# def show(revNo):
#     return "You Entered %f" % revNo


# @app.route('/blog/<int:postID>')
# def show_blog(postID):
#    return 'Blog Number %d' % postID
#
# @app.route('/rev/<float:revNo>')
# def revision(revNo):
#    return 'Revision Number %f' % revNo

# @app.route('/admin')
# def hello_admin():
#     return 'Hello Admin'
#
# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return "Hello %s you are logged in as Guest" %guest
#
# @app.route('/user/<username>')
# def check(username):
#     if username=='admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest',guest=username))


# @app.route('/sucess/<name>')
# def print_s(name):
#     return render_template('view.html',username=name)
#
#
# @app.route('/login',methods=['POST','GET'])
# def login():
#     if request.method=='POST':
#         user = request.form
#         print('request type: POST')
#         print(user)
#         return redirect(url_for('print_s',name=user))
#     else:
#         user = request.args.get
#         print('request Type: GET:')
#         print(user)
#         return redirect(url_for('print_s',name=user))
#
# @app.route('/result',methods=['POST','GET'])
# def result():
#     if request.method == 'POST':
#         result= request.form
#         return render_template('result.html',result=result)
#
#
# @app.route('/view')
# def view():
#     return render_template('view.html')

# app.secret_key = "any random string"
#
# @app.route('/')
# def index():
#    if 'username' in session:
#       username = session['username']
#       return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
#    return "You are not logged in <br><a href = '/login'></b>" +"click here to log in</b></a>"
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#
#    <form action = "" method = "post">
#       <p><input type ="text" name = "username"/></p>
#       <p><input type = "submit" value = "Login"/></p>
#    </form>
#    '''
#
# @app.route('/logout')
# def logout():
#    # remove the username from the session if it is there
#    session.pop('username', None)
#    return redirect(url_for('index'))


#
# @app.route('/')
# def index():
#    return render_template('index.html')
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or \
#                         request.form['password'] != 'admin':
#             error = 'Invalid username or password. Please try again!'
#         else:
#             flash('You were successfully logged in')
#             return redirect(url_for('index'))
#     return render_template('login.html', error=error)
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'random string'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                        request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))

    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)