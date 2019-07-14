# integrasi mysql ke python-flask

# pip install namaPackage
# pip install <flask> flask_mysqldb flask_cors / python -m pip install flask flask_mysqldb flask_cors
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import base64

app=Flask(__name__)
mysql=MySQL(app)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='agammsantos'
app.config['MYSQL_PASSWORD']=base64.b64decode(b"RGFuY2VyMTE5OQ==").decode('utf-8')
app.config['MYSQL_DB']='tes_flask'

@app.route('/')
def home():
    return jsonify({'status':'Selamat datang!'})

@app.route('/data')
def data():
    x=mysql.connection.cursor()
    x.execute('select * from mytable')
    data=x.fetchall()
    print(data)
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

@app.route('/data/<path:id>') # atau gunakan <string:id>
def dataSatuan(id):
    x=mysql.connection.cursor()
    x.execute('select * from mytable where id='+id)
    data=x.fetchall()
    print(data)
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