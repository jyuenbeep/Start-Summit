from flask import Flask, request
from flask import render_template
from flask import request
from flask import session
import sqlite3
from db import model_specified, createArray
from password import create_password, analyze_password
from figure import plot

import io
from flask import Response
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# import numpy as np
# import matplotlib.pyplot as plt
import matplotlib

matplotlib.pyplot.switch_backend('Agg')

app = Flask(__name__)
app.secret_key = "23bd2dcea35c795e204d397157f3d55bf1afda7db6519a46f9d1e5a5f02ed45b"

# MAKING TABLES ======================================================================

html_template = """
<!DOCTYPE html>
<html>
    <head>
        <script src="../static/js/slider.js" defer> </script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    </head>
    <body>
        <div>
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">Trends of Vulnerable Data in Big Corporations</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/stats">Statistics</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/quiz">Quiz</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/aboutus">About Us</a>
                </li>
            </ul>
        </div>
        </nav>
        </div>
        <div>
            <image src="static/my_plot.png" class="img-fluid"></image>
            <h1 class="text-center">Statistics Table</h1>
            <form action="/tablePage" method="POST" class="d-flex align-items-center flex-column">
                <div class="slider-container d-flex justify-content-center" style="width:100%">
                    <label for="recordMin"><b>Minimum # of Records Lost</b></label> : <span id="recordMin_value"></span>
                    <input type="range" min="100000" max="5000000" value="100000" class="form-range" id="recordMin" name="recordMin" style="width:80%">
                </div>
                <div class="slider-container d-flex justify-content-center" style="width:100%">
                    <label for="yearMin"><b>Start Year</b></label> : <span id="yearMin_value"></span>
                    <input type="range" min="2011" max="2022" value="2011" class="form-range" id="yearMin" name="yearMin" style="width:80%">
                </div>
                <button type="submit" class="btn btn-secondary btn-lg btn-sm" value="submit"> Submit Table </button><br>
            </form>
        </div>
        <div>
            <table class="table table-hover">
                {DATA_TABLE}
            </table>
        </div>
    </body>
</html>
"""

def makeRecordTable(rMin, yMin):
    dataDict = model_specified(["records lost", "date", "sector", "data sensitivity"], rMin, yMin)
    htmlTable = """
        <tr class="thead-dark">
            <th scope="row">Organization</th>
            <th># of Records Lost</th>
            <th>Date of Breach</th>
        </tr>
    """
    for element in dataDict:
        org = dataDict[element]   
        htmlTable+=f"""
        <tr>
            <th scope="row">{element}</th>
            <td>{org[0]}</td>
            <td>{org[1]}</td>
        </tr>
        """
    return htmlTable

def writeHTML(htmlTemplate, file):
    with open("templates/"+file, 'w') as f:
        f.write(htmlTemplate)
    f.close()

# FLASK APP ROUTING ==================================================================

@app.route("/", methods=['GET'])
def homepage():
    return render_template('home.html')

@app.route("/aboutus", methods=['GET'])
def aboutpage():
    return render_template('aboutus.html')

@app.route("/resources", methods=['GET'])
def resourcespage():
    return render_template('resources.html')

@app.route("/quiz", methods=['GET'])
def quizpage():
    return render_template('quiz.html')

@app.route("/password", methods=['GET'])
def passwordpage():
    return render_template('password.html')

@app.route("/game", methods=['GET'])
def passwordpage():
    return render_template('game.html')

@app.route("/analyzepass", methods=['GET', 'POST'])
def analyzepasspage():
    feedback = ""
    if (request.method=="POST"):
        uInput = request.form.get("user_input")
        if (uInput!=""):
            feedback = analyze_password(uInput)
    return render_template('password.html', FEEDBACK=feedback)

@app.route("/genpass", methods=['GET', 'POST'])
def genpasspage():
    passGen = ""
    if (request.method=="POST"):
        uInput = request.form.get("user_input")
        if (uInput!=""):
            passGen = create_password(uInput)
    return render_template('password.html', NEW_PASS=passGen)

@app.route("/stats", methods=["GET", "POST"])
def statspage():
    return render_template("stats.html")

@app.route("/tablePage", methods=["GET", "POST"])
def statsTablePage():
    if (request.method=="POST"):
        recordMin = int(request.form.get("recordMin"))
        yearMin = int(request.form.get("yearMin"))
        # matplotlib
        dataDict = model_specified(["records lost", "year   "], recordMin, yearMin)
        arr = createArray(dataDict)
        plot(arr, len(arr[0]))
        # making table and overwriting into HTML
        table = makeRecordTable(recordMin, yearMin)
        writeHTML(html_template.format(DATA_TABLE=table), "table.html")
    else:
        table = makeRecordTable(0, 0)
        writeHTML(html_template.format(DATA_TABLE=table), "table.html")
    return render_template("table.html")
    
# RUN ================================================================================

if __name__ == "__main__":
    app.debug = True
    app.run()




