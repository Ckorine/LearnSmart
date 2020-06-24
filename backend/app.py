from flask import Flask, render_template, request, session, url_for, redirect
import bcrypt
from datetime import datetime

from flask_pymongo import PyMongo
from mongoengine import connect

from User import User
from registerForm import register
from loginForm import loginForm

app = Flask(__name__)
app.secret_key = 'development key'
app.config['MONGO_URI'] = "mongodb://localhost:27017/Person"
app.config['MONGO_DBNAME'] = "Person"
mongo = PyMongo(app)
loggedIn = 'notloggedIn'

connect('Person', host='localhost', port=27017)


@app.route('/')
def index():
    return render_template('base.html', loggedIn='notloggedIn')


@app.route('/home')
def home():
    if not session.get("email") is None:
        return render_template('base.html', loggedIn='loggedIn')
    return render_template('base.html', loggedIn='notloggedIn')


@app.route('/profil')
def profil():
    if not session.get("email") is None:
        loggedIn = 'loggedIn'
        email = session.get("email")
        users = mongo.db.user
        existing_user = users.find_one({'email': email})
        print(existing_user)
        return render_template("profil.html", userInfo=existing_user, loggedIn=loggedIn)
    else:

        print("No email found in session")
        return redirect(url_for("login"))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = register()
    if request.method == 'POST':
        user = mongo.db.user
        existing_user = user.find_one({'email': request.form['email']})

        if existing_user is None:
            password = request.form.get('password')
            confirmPassword = request.form.get('confirm')
            if len(password) >= 6:
                if password is not confirmPassword:
                    user = User(
                        firstname=request.form.get("firstname"),
                        lastname=request.form.get("lastname"),

                        birthdate=datetime.strptime(
                            request.form.get("birthdate"), '%Y-%m-%d'),
                        email=request.form.get("email"),
                        password=bcrypt.hashpw(request.form.get(
                            "password").encode('utf-8'), bcrypt.gensalt())

                    )
                    user.save()
                    return 'you have successfully registerted,'
                return 'Passwords must match!'
            return 'Passwords length must greater than 5!'
        return 'That username already exists!'
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    loggedIn = 'notloggedIn'
    form = loginForm()
    if request.method == 'POST':

        user = mongo.db.user
        login_user = user.find_one({'email': request.form.get('email')})

        if login_user:
            if bcrypt.checkpw(request.form.get('password').encode('utf-8'), login_user['password'].encode('utf-8')):
                session['email'] = request.form['email']
                session['firstname'] = login_user['firstname']
                session['lastname'] = login_user['lastname']
                session['birthdate'] = login_user['birthdate']
                loggedIn = 'loggedIn'

                print(session)
                return redirect(url_for("profil"))

        return 'Invalid email/password combination'
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    form = loginForm()
    loggedIn = 'notloggedIn'
    return render_template('login.html', form=form, loggedIn=loggedIn)


# @app.route('/profil', methods=['GET', 'POST'])
# def logout():


if __name__ == "__main__":
    app.run(debug=True)