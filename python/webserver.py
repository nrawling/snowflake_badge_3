from flask import Flask
from snowflake import connector
import keyring

app = Flask("my website")

@app.route('/')
def homepage():
    return "Welcome to my website! My Snowflake Acct # is " + str(onerow)

# Snowflake
cnx = connector.connect(
    account='xt70683.us-central1.gcp',
    user='nathanrawling',
    password=keyring.get_password('snowflake','badge3')
)
cur = cnx.cursor()
cur.execute("SELECT current_account()")
onerow = cur.fetchone()

app.run()
