from flask import render_template
#import backend.py


def make_endpoints(app):

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
    @app.route("/signup")
    def signUpPage():
        return render_template("sign_up.html")
    @app.route("/login")
    def logInPage():
        return render_template("log_in.html")
    @app.route("/logout")
    def logOutPage():
        return render_template("log_out.html")
    @app.route("/upload")
    def uploadPage():
        return render_template("upload.html")

    #@app.route("/pages/<stored>")
    #def grabUploaded(stored):
    #    needPage = get_wiki_page(stored)
    #    return render_template(needPage)