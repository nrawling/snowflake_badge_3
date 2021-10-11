from snowflake import connector
import keyring
import pandas as pd

# Snowflake
def sfconnect():
    cnx = connector.connect(
        account='xt70683.us-central1.gcp',
        user='nathanrawling',
        password=keyring.get_password('snowflake','badge3'),
        warehouse='COMPUTE_WH',
        database='DEMO_DB',
        schema='PUBLIC')
    return cnx
