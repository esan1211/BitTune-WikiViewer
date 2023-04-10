from flask import render_template, request, redirect, url_for, session
from flaskr.backend import Backend
from werkzeug.utils import secure_filename
import base64
import io
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

    @app.route("/about") #Enrique
    def about():
        if request.method == 'GET':
            img1 = backend.get_image("asis.jpeg")
            img2 = backend.get_image("daniel.JPG")
            img3 = backend.get_image("enrique.jpg")
            img1 = img1.decode('UTF-8')
            img2 = img2.decode('UTF-8')
            img3 = img3.decode('UTF-8')
        return render_template("about.html", img1 = img1, img2 = img2, img3 = img3)
    
    @app.route("/signup", methods = ['GET', 'POST']) #Asis
    def sign_up_page():
        msg = ''

        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            user = request.form['username']
            password = request.form['password']
            
            if not backend.sign_up(user, password):
                msg = 'You already have an account, Click Login!'
            else:
                msg = 'Your sign up was successful, Click Login!'

        return render_template("signup.html", msg = msg) #Asis
    
    
    @app.route("/login", methods = ['GET', 'POST']) #Asis
    def login_page():
        msg = ''

        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            user = request.form['username']
            password = request.form['password']

            if backend.sign_in(user, password) is True:
                return render_template('logged_in.html', msg = msg, name = user)   
            else:
                msg = 'Incorrect username or password'              

        return render_template("login.html", msg = msg) #Asis
    
    @app.route("/logout") #Asis
    def logout_page():
        return render_template('main.html')

    @app.route("/upload", methods = ['GET','POST']) #Enrique
    def uploadPage():
        #app.config['UPLOAD_FILE'] = "/home/username/project/"
        if request.method == "POST":
            
            if request.files:
                f = request.files["myfile"]
                
                if f.filename == '':
                    print("File cannot be empty")
                    return redirect(request.url)
                
                basedir = os.path.abspath(os.path.dirname(__file__))
                filename = secure_filename(f.filename)
                basedir = os.path.dirname(basedir)
                f.save(os.path.join(os.path.join(basedir),filename))
                backend.upload(filename)
                os.remove(f.filename)
                return render_template("upload.html")
                
        return render_template("upload.html")

    @app.route("/pages/<stored>") #Danny
    def grabUploaded(stored):
        neededPage = backend.get_wiki_page(stored)
        return neededPage #render_template(neededPage)