from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename
import os
from pymongo import MongoClient
import base64

x=MongoClient('mongodb://localhost:27017/')
db=x['test']
col=db['user']

app=Flask(__name__)
app.config['upload_folder']='storage'

@app.route('/')
def home():
    return '<h1>Selamat datang!</h1>'

@app.route('/soalform')
def form():
    return render_template('soalformulir.htm')

@app.route('/dataku',methods=['POST','GET'])
def dataku():
    if request.method=='GET':
        for x in col.find():
            print(x)
    elif request.method=='POST':
        nama=request.form['haha']
        usia=request.form['hihi']
        if not request.files.get('hehe', None):
            data={'nama':nama,'usia':int(usia),'img':'http://localhost:5000/upload/0.jpg'}
            z=col.insert_one(data)
            for i in col.find({'_id':z.inserted_id}):
                print('Data sukses tersimpan!')
                print(i)
            return redirect(url_for('suksesUpload'))
        else:
            gambar=request.files['hehe']
            namafile=secure_filename(gambar.filename)
            pathfile='http://localhost:5000/upload/'+namafile
            gambar.save(os.path.join(app.config['upload_folder'],namafile))
            data={'nama':nama,'usia':int(usia),'img':pathfile}
            z=col.insert_one(data)
            for i in col.find({'_id':z.inserted_id}):
                print('Data sukses tersimpan!')
                print(i)
            return redirect(url_for('suksesUpload'))

@app.route('/success')
def suksesUpload():
    for x in col.find().sort([('$natural',-1)]).limit(1): # sort dalam pymongo harus dalam bentuk list of key-direction pairs
        filebaru=[x['_id'],x['nama'],x['usia'],x['img']]
    return render_template('upload.htm',y=filebaru)

@app.route('/akun')
def akun():
    if 'nama' in request.args:
        carinama=request.args['nama']
        for x in col.find({'nama':carinama}):
            filedipilih=[x['_id'],x['nama'],x['usia'],x['img']]
        return render_template('upload.htm', y=filedipilih)

@app.route('/upload/<path:x>')
def hasilUpload(x):
    return send_from_directory('storage',x)

if __name__=='__main__':
    app.run(debug=True)