import pandas as pd
import numpy as np
import mysql.connector
import base64

mydb=mysql.connector.connect(
    host='localhost',
    user='agammsantos',
    passwd=base64.b64decode(b"RGFuY2VyMTE5OQ==").decode('utf-8'),
    database='fauna'
)

query='select * from aves'
df=pd.read_sql(query,con=mydb)
print(df.set_index('id'))