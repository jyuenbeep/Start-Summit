from flask import Flask, request
from flask import render_template
from flask import request
from flask import session
import sqlite3
from db import model_specified

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
            <form action="/stats_table" method="POST">
                <label for="recordMin">Minimum # of Records Lost</label><br>
                <div class="slider-container">
                    <input type="range" min="100000" max="5000000" value="100000" class="slider" id="recordMin" name="recordMin">
                    <span id="min_value"></span>
                </div>
                <button type="submit" class="btn" value="submit"> Submit Table </button>
            </form>
        </div>
        <div>
            <table>
                {DATA_TABLE}
                {MIN_VALUE}
            </table>
        </div>
    </body>
</html>
"""

def makeRecordTable(min):
    dataDict = model_specified(["records lost", "date"], min)
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

@app.route("/analyzepass", methods=['GET'])
def analyzepasspage():
    return render_template('analyzepass.html')

@app.route("/genpass", methods=['GET'])
def genpasspage():
    return render_template('genpass.html')

@app.route("/stats_table", methods=["GET", "POST"])
def statspage():
    if (request.method=="POST"):
        recordMin = int(request.form.get("recordMin"))
        table = makeRecordTable(recordMin)
        writeHTML(html_template.format(DATA_TABLE=table, MIN_VALUE=recordMin), "stats.html")
    else:
        table = makeRecordTable(0)
        writeHTML(html_template.format(DATA_TABLE=table, MIN_VALUE=0), "stats.html")
    return render_template("stats.html")
    
# RUN ================================================================================

if __name__ == "__main__":
    app.debug = True
    app.run()




