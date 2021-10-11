from flask import Flask, render_template
from snowflake import connector
import keyring
import pandas as pd

app = Flask("my website")

@app.route('/')
def homepage():
    return render_template("index.html", dfhtml=dfhtml)

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
