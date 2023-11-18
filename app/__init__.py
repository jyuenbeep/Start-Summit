from flask import Flask, request
from flask import render_template
from flask import request
from flask import session
import sqlite3
from db import model_specified
from password import create_password, analyze_password

app = Flask(__name__)
app.secret_key = "23bd2dcea35c795e204d397157f3d55bf1afda7db6519a46f9d1e5a5f02ed45b"

# MAKING TABLES ======================================================================

html_template = """
<!DOCTYPE html>
<html>
    <head>
        <script src="../static/js/slider.js" defer> </script>
    </head>
    <body>
        <h1>Statistics Table</h1>
        <div>
            <form action="/stats" method="POST">
                <label for="recordMin">Minimum # of Records Lost</label><br>
                <div class="slider-container">
                    <input type="range" min="100000" max="5000000" value="100000" class="slider" id="recordMin" name="recordMin">
                    <span id="recordMin_value"></span>
                </div>
                <label for="yearMin">Start Year</label><br>
                <div class="slider-container">
                    <input type="range" min="2011" max="2022" value="2011" class="slider" id="yearMin" name="yearMin">
                    <span id="yearMin_value"></span>
                </div>
                <button type="submit" class="btn" value="submit"> Submit Table </button>
            </form>
        </div>
        <div>
            <table>
                {DATA_TABLE}
            </table>
        </div>
    </body>
</html>
"""

def makeRecordTable(rMin, yMin):
    dataDict = model_specified(["records lost", "date", "sector", "data sensitivity"], rMin, yMin)
    htmlTable = """
        <tr>
            <th>Organization</th>
            <th># of Records Lost</th>
            <th>Date of Breach</th>
        </tr>
    """
    for element in dataDict:
        org = dataDict[element]   
        htmlTable+=f"""
        <tr>
            <td>{element}</td>
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

@app.route("/analyzepass", methods=['GET', 'POST'])
def analyzepasspage():
    feedback = ""
    if (request.method=="POST"):
        uInput = request.form.get("user_input")
        if (uInput!=""):
            feedback = analyze_password(uInput)
    return render_template('analyzepass.html', FEEDBACK=feedback)

@app.route("/genpass", methods=['GET', 'POST'])
def genpasspage():
    passGen = ""
    if (request.method=="POST"):
        uInput = request.form.get("user_input")
        if (uInput!=""):
            passGen = create_password(uInput)
    return render_template('genpass.html', NEW_PASS=passGen)

@app.route("/stats", methods=["GET", "POST"])
def statspage():
    if (request.method=="POST"):
        recordMin = int(request.form.get("recordMin"))
        yearMin = recordMin = int(request.form.get("yearMin"))
        table = makeRecordTable(recordMin, yearMin)
        writeHTML(html_template.format(DATA_TABLE=table), "stats.html")
    else:
        table = makeRecordTable(0, 0)
        writeHTML(html_template.format(DATA_TABLE=table), "stats.html")
    return render_template("stats.html")
    
# RUN ================================================================================

if __name__ == "__main__":
    app.debug = True
    app.run()




