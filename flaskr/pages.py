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
        page_name_list = backend.get_all_page_names()
        return render_template("pages.html", name_lst = page_name_list)

    @app.route("/about")
    def about():
        return render_template("about.html")
    
    @app.route("/signup", methods = ['GET', 'POST']) #Asis
    def sign_up_page():
        msg = ''

        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            user = request.form['username']
            password = request.form['password']
            
            if backend.sign_up(user, password) == False:
                msg = 'You already have an account!'
            elif not user or not password:
                msg = 'Create an account by entering a username and password!'
            else:
                msg = 'Your sign up was successful!'
        
        elif request.method == 'POST':
            msg = 'Create an account by entering a username and password!'

        return render_template("signup.html", msg = msg) #Asis
    
    
    @app.route("/login", methods = ['GET', 'POST']) #Asis
    def login_page():
        msg = ''

        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            user = request.form['username']
            password = request.form['password']

            if backend.sign_in(user, password) == True:
                session['loggedin'] = True
                session['username'] = user
                msg = 'You are logged in !'
                return render_template('main.html', msg = msg)
            else:
                msg = 'Incorrect username or password'
        
        return render_template("login.html", msg = msg) #Asis
    
    @app.route("/logout") #Asis
    def logout_page():
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
        neededPage = backend.get_wiki_page(stored)
        return neededPage #render_template(neededPage)
