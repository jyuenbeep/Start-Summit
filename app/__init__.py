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
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">
        <script src="../static/js/slider.js" defer> </script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    </head>
    <body style="background-color:#f4f1de">
        <div>
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="/"><strong>SECUREHUB</strong></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="/">HOME <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/stats">STATISTICS</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/resources">RESOURCES</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/password">PASSWORDS</a>
        </li>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/quiz">QUIZ</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/game">GAME</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/aboutus">ABOUT US</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/contact">CONTACT</a>
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
            <div class="d-flex justify-content-center">
                <div class="card table-wrapper-scroll-y my-custom-scrollbar rounded-1" style="width:50%">
                    <table class="table table-bordered table-hover rounded-10">
                        {DATA_TABLE}
                    </table>
                </div>
            </div>
        </div>
    </body>
</html>
"""
def makeRecordTable(rMin, yMin):
    dataDict = model_specified(["records lost", "date", "sector", "data sensitivity"], rMin, yMin)
    htmlTable = """
    <thead class="custom-header sticky-top">
        <tr>
            <th scope="col" class="text-white">Organization</th>
            <th scope="col" class="text-white"># of Records Lost</th>
            <th scope="col" class="text-white">Date of Breach</th>
        </tr>
            </thead>
                    <tbody>
    """
    for element in dataDict:
        org = dataDict[element]
        htmlTable += f"""
            <tr class="table-light">
                <th scope="row">{element}</th>
                <td>{org[0]}</td>
                <td>{org[1]}</td>
            </tr>
        """
      
    htmlTable += """
        </tbody>
        <style>
            .custom-header {
                background-color: #3D405B;
            }
        </style>
        
    """
    return htmlTable

def writeHTML(htmlTemplate, file):
    with open("templates/"+file, 'w', encoding='utf-8') as f:
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

@app.route("/contact", methods=['GET'])
def contactpage():
    return render_template('contact.html')

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
        # print(arr)
        # making table and overwriting into HTML
        table = makeRecordTable(recordMin, yearMin)
        writeHTML(html_template.format(DATA_TABLE=table), "table.html")
    else:
        table = makeRecordTable(0, 0)
        # print(table)
        writeHTML(html_template.format(DATA_TABLE=table), "table.html")
    return render_template("table.html")


@app.route("/game", methods=['GET'])
def gamepage():
    return render_template('game.html')

@app.route("/page1", methods=['GET'])
def page1page():
    return render_template('game/page1.html')

@app.route("/page2a", methods=['GET'])
def page2apage():
    return render_template('game/page2a.html')

@app.route("/page2b", methods=['GET'])
def page2bpage():
    return render_template('game/page2b.html')

@app.route("/getgame1a", methods=['GET'])
def getgame1apage():
    return render_template('game/get_game1a.html')

@app.route("/getgame1b", methods=['GET'])
def getgame1bpage():
    return render_template('game/get_game1b.html')

@app.route("/getgame2a", methods=['GET'])
def getgame2apage():
    return render_template('game/get_game2a.html')

@app.route("/pageshutdown", methods=['GET'])
def pageshutdownpage():
    return render_template('game/page_shutdown.html')

@app.route("/popup1a", methods=['GET'])
def popup1apage():
    return render_template('game/popup1a.html')

@app.route("/popup1b", methods=['GET'])
def popup1bpage():
    return render_template('game/popup1b.html')

@app.route("/popup2a", methods=['GET'])
def popup2apage():
    return render_template('game/popup2a.html')
    
# RUN ================================================================================

if __name__ == "__main__":
    app.debug = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0')




