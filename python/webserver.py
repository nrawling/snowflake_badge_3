from flask import Flask, render_template, request
from snowflake import connector
import keyring
import pandas as pd

app = Flask("my website")

@app.route('/')
def homepage():
    return render_template("index.html", dfhtml=dfhtml)

@app.route('/submit')
def submitpage():
    return render_template('submit.html')

@app.route('/thanks4submit', methods=["POST"])
def thanks4submit():
    colorname = request.form.get("cname")
    username = request.form.get("uname")
    cnx.cursor().execute("INSERT INTO COLORS(COLOR_UID, COLOR_NAME) " +
        "SELECT COLOR_UID_SEQ.nextval, '" + colorname + "'")
    return render_template("thanks4submit.html"
                           ,colorname=colorname
                           ,username=username)

# Snowflake
cnx = connector.connect(
    account='xt70683.us-central1.gcp',
    user='nathanrawling',
    password=keyring.get_password('snowflake','badge3'),
    warehouse='COMPUTE_WH',
    database='DEMO_DB',
    schema='PUBLIC'
)
cur = cnx.cursor()
cur.execute("SELECT * FROM COLORS")
rows=pd.DataFrame(cur.fetchall(),columns=['Color UID','Color Name'])

# test dataframe as html
dfhtml = rows.to_html()

app.run()
