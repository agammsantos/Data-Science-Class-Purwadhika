# menginstal connector mysql tanpa flask_mysqldb
# pip install MySQL-connector-python

from flask import Flask, jsonify
import mysql.connector
import base64

app=Flask(__name__)

@app.route('/data')
def data():
    mydb=mysql.connector.connect(
        host='localhost',
        user='agammsantos',
        password=base64.b64decode(b"RGFuY2VyMTE5OQ==").decode('utf-8'),
        database='tes_flask'
    )

    x=mydb.cursor()
    x.execute('select * from mytable')
    data=x.fetchall()

    print(data)
    
    allData=[]
    for i in range(len(data)):
        id=data[i][0]
        nama=data[i][1]
        usia=data[i][2]
        dataDict={
            "id":id,
            "nama":nama,
            "usia":usia
        }
        allData.append(dataDict)
    
    print(allData)
    return jsonify(allData)


@app.route('/data/<path:id>') # atau gunakan <string:id>
def dataSatuan(id):
    mydb=mysql.connector.connect(
        host='localhost',
        user='agammsantos',
        password=base64.b64decode(b"RGFuY2VyMTE5OQ==").decode('utf-8'),
        database='tes_flask'
    )

    x=mydb.cursor()
    x.execute(f'select * from mytable where id={id}')
    data=x.fetchall()
    print(type(data))

    allData=[]
    for i in range(len(data)):
        id=data[i][0]
        nama=data[i][1]
        usia=data[i][2]
        dataDict={
            "id":id,
            "nama":nama,
            "usia":usia
        }
        allData.append(dataDict)
    
    print(allData)
    return jsonify(allData)    

if __name__=='__main__':
    app.run(debug=True)