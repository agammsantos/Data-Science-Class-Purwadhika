import json
from flask import Flask, render_template, request, jsonify, redirect, url_for

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.htm')

@app.route('/signup')
def signup():
    return render_template('signup.htm')

@app.route('/signup/sukses',methods=['POST'])
def sukses():
    nama=request.form['nama']
    pswd=request.form['pass']
    user={'id':nama,'ps':pswd}
    with open('data.json') as dataku:
        print(type(dataku))
        data=json.load(dataku)
    with open('data.json') as dataku:
        data=json.load(dataku)
    data.append(user)
    datafix=json.dumps(data)
    jsonku=open('data.json','w')
    jsonku.write(datafix)
    return 'Akun terdaftar silahkan login kembali'

@app.route('/signin', methods=['POST'])
def signin():
    name=request.form['nama']
    pswd=request.form['pass']
    with open('data.json') as dataku:
        print(type(dataku))
        data=json.load(dataku)
    i=0
    if len(data)==0:
        return '<h1>Nama dan password tidak terdaftar</h1>'
    else:
        while i<len(data):
            if name!=data[i]['id'] or pswd!=data[i]['ps']:
                i+=1
                if i==len(data):
                    return '<h1>Nama dan password tidak terdaftar</h1>'
                    break
            elif name==data[i]['id'] and pswd==data[i]['ps']:
                return redirect(url_for('profile',nama=name))
                break

@app.route('/<string:nama>')
def profile(nama):
    return 'Selamat datang '+nama

@app.errorhandler(404)
def error404(error):
    return '<h1>Error: 404 Not Found</h1>'

if __name__=='__main__':
    app.run(debug=True)