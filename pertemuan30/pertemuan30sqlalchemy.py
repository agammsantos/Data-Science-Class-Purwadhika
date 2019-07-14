# pip install sqlalchemy pymysql

import numpy as np
import pandas as pd
import sqlalchemy
import base64

mydb=sqlalchemy.create_engine(
    # namaDBsys://user:pass@host:port/namaDatabase
    'mysql+pymysql://agammsantos:'+base64.b64decode(b"RGFuY2VyMTE5OQ==").decode('utf-8')+'@localhost:3306/fauna'
)

query='select * from aves'
df=pd.read_sql(query,mydb)
print(df)