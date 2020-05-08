###############################################################################
# Name : Katie Tsui
# Uni : kft2108
#
# File contains app routes for three web pages: home, assignment, and course.
###############################################################################

#import statements
from flask import Flask, render_template
import requests
import bs4
import pandas as pd
import numpy as np

#Flask app variable
app = Flask(__name__)


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

#datamining route
@app.route("/data")
def datamining():
    bs=bs4.BeautifulSoup(requests.get('https://www.worldometers.info/coronavirus/').content, 'lxml')
    tables=bs.find_all('table')
    main_table=pd.read_html(str(tables[0]))[0]
    main_table = main_table.replace(np.nan, '', regex=True)
    return render_template('data.html', tables=[main_table.to_html()])

#start the server
if __name__ == "__main__":
    app.run()