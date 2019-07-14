from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename
import os
from flask_mysqldb import MySQL
import base64

app=Flask(__name__)
app.config['upload_folder']='storage'
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
        jml=x.execute('select * from akun')
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
                img=data[i][3]
                dataDict={
                    "id":id,
                    "nama":nama,
                    "usia":usia,
                    "img":img
                }
                allData.append(dataDict)
            
            print(allData)
            return jsonify(allData)
        else:
            return jsonify({'status':'tidak ada data'})

    elif request.method=='POST':
        nama=request.form['haha']
        usia=request.form['hihi']
        if not request.files.get('hehe', None):
            x=mysql.connection.cursor()
            x.execute('insert into akun (nama,usia) values (%s,%s)',(nama,usia))
            mysql.connection.commit()
            return redirect(url_for('suksesUpload')) # alternatif cara
        else:
            gambar=request.files['hehe']
            namafile=secure_filename(gambar.filename)
            pathfile='http://localhost:5000/upload/'+namafile
            gambar.save(os.path.join(app.config['upload_folder'],namafile))
            x=mysql.connection.cursor()
            x.execute('insert into akun (nama,usia,img) values (%s,%s,%s)',(nama,usia,pathfile))
            mysql.connection.commit()
            return redirect(url_for('suksesUpload'))

@app.route('/success')
def suksesUpload():
    x=mysql.connection.cursor()
    jml=x.execute('select * from akun')
    print(jml)
    if jml>0:
        data=x.fetchall()
        allData=[]
        for i in range(len(data)):
            id=data[i][0]
            nama=data[i][1]
            usia=data[i][2]
            img=data[i][3]
            dataDict={
                "id":id,
                "nama":nama,
                "usia":usia,
                "img":img
            }
            allData.append(dataDict)

    filebaru=[allData[-1]['id'],allData[-1]['nama'],allData[-1]['usia'],allData[-1]['img']]
    return render_template('upload.htm', y=filebaru)

@app.route('/akun')
def akun():
    if 'id' in request.args or 'nama' in request.args or 'usia' in request.args:
        x=mysql.connection.cursor()
        jml=x.execute('select * from akun')
        if jml>0:
            data=x.fetchall()
            allData=[]
            for i in range(len(data)):
                id=data[i][0]
                nama=data[i][1]
                usia=data[i][2]
                img=data[i][3]
                dataDict={
                    "id":id,
                    "nama":nama,
                    "usia":usia,
                    "img":img
                }
                allData.append(dataDict)
            if 'id' in request.args:
                id=int(request.args['id'])
                if id<1 or id>len(allData):
                    return 'Maaf data tidak ditemukan'
                else:
                    filedipilih=[allData[id-1]['id'],allData[id-1]['nama'],allData[id-1]['usia'],allData[id-1]['img']]
                    return render_template('upload.htm', y=filedipilih)


@app.route('/upload/<path:x>')
def hasilUpload(x):
    return send_from_directory('storage',x)

@app.route('/soalform')
def form():
    return render_template('soalformulir.htm')


if __name__=='__main__':
    app.run(debug=True)