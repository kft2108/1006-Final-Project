###############################################################################
# Name : Katie Tsui
# Uni : kft2108
#
# File contains app routes for three web pages: home, assignment, and course.
###############################################################################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template("index.html")

#additional route
@app.route("/assignment")
def assignment():
    return render_template("assignment.html")

#additional route
@app.route("/course")
def course():
    return render_template("course.html")

#start the server
if __name__ == "__main__":
    app.run()