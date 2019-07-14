from flask import Flask, jsonify, request, render_template
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
    return '<h1>Selamat datang!</h1>'

@app.route('/dataku',methods=['POST','GET'])
def dataku():
    if request.method=='GET':
        x=mysql.connection.cursor()
        jml=x.execute('select * from mytable')
        print(jml)
        if jml>0:
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
        else:
            return jsonify({'status':'tidak ada data'})

    elif request.method=='POST':
        # asd = request.json # mengirim/post lewat postman dari kolom body-raw-json dalam bentuk list of dictionaries/json
        # for i in asd:
        #     nama = i['nama']
        #     usia = i['usia']
        #     x=mysql.connection.cursor()
        #     x.execute('insert into mytable (nama,usia) values (%s,%s)',(nama,usia))
        #     mysql.connection.commit()
        nama=request.form['haha']
        usia=request.form['hihi']
        x=mysql.connection.cursor()
        x.execute('insert into mytable (nama,usia) values (%s,%s)',(nama,usia))
        mysql.connection.commit()
        return jsonify({'status':'Anda nge-POST'})
    # else:
    #     return jsonify({'status':'Anda tidak GET atau POST'})

@app.route('/form')
def form():
    return render_template('formulir.htm')


if __name__=='__main__':
    app.run(debug=True)