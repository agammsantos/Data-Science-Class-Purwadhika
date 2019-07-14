from flask import redirect,Flask,request,send_from_directory,url_for,render_template
import numpy as np
import pandas as pd
import json, requests
import joblib

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.htm')

@app.route('/hasil',methods=['POST'])
def hasil():
    usia=int(request.form['usia'])
    kamar=int(request.form['kamar'])
    luas=int(request.form['luas'])
    model=joblib.load('modelJoblib')
    harga=model.predict([[usia,kamar,luas]])
    a=format(int(round(harga[0])),',').replace(',','.')
    return f'Harga rumah anda adalah Rp {a},00'

if __name__=='__main__':
    app.run(debug=True)