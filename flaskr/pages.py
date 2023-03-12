from flask import render_template, request, redirect, url_for, session
from flaskr.backend import Backend
from werkzeug.utils import secure_filename
import os


def make_endpoints(app):
    backend = Backend()
    
    # Flask uses the "app.route" decorator to call methods when users
    # go to a specific route on the project's website.
    @app.route("/")
    def home():
        return render_template("main.html")

    # TODO(Project 1): Implement additional routes according to the project requirements.
    @app.route("/pages")
    def pages():
        return render_template("pages.html")
    @app.route("/about")
    def about():
        return render_template("about.html")
    
    @app.route("/signup", methods = ['GET', 'POST']) #Asis
    def signUpPage():
        message = ''
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            user = request.form['username']
            password = request.form[password]
            
            if backend.sign_up(user, password) == False:
                message = 'You already have an account!'
            elif not user or not password:
                message = 'Create an account by entering a username and password!'
            else:
                'Your registration was successful!'
        elif request.method == 'POST':
            message = 'Create an account by entering a username and password!'

        return render_template("signup.html", msg = message) #Asis
    
    @app.route("/")
    @app.route("/login", methods = ['GET', 'POST']) #Asis
    def logInPage():
        message = ''
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            user = request.form['username']
            password = request.form['password']

            if backend.sign_in(user, password) == True:
                session['loggedin'] = True
                session['username'] = user
                message = 'You are logged in !'
                return render_template('main.html', msg = message)
            else:
                message = 'Incorrect username or password'
        
        return render_template("login.html", msg = message) #Asis
    
    @app.route("/logout") #Asis
    def logOutPage():
        session.pop('loggedin', None)
        session.pop('username', None)
        return redirect(url_for('login'))


    @app.route("/upload", methods = ['GET','POST']) #Enrique
    def uploadPage():
        print('hi')
        app.config['UPLOAD_FILE'] = "/home/enrique_munoz/project/"
        if request.method == "POST":
            
            if request.files:
                print(request.files)
                f = request.files["myfile"]
                
                if f.filename == '':
                    print("File cannot be empty")
                    return redirect(request.url)
                
                basedir = os.path.abspath(os.path.dirname(__file__))
                filename = secure_filename(f.filename)
                f.save(os.path.join(os.path.join(basedir,app.config['UPLOAD_FILE'],filename)))
                backend.upload(f.filename)
                os.remove(f.filename)
                return render_template("upload.html")
                
        return render_template("upload.html")

    @app.route("/pages/<stored>") #Danny
    def grabUploaded(stored):
        needPage = backend.get_wiki_page(stored)
        return render_template(needPage)
