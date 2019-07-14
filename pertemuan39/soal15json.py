from flask import Flask, request, jsonify, render_template
import numpy as np
import json
import joblib as jb

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.htm')

@app.route('/prediksi')
def prediksi():
    return render_template('prediksi.htm')

@app.route('/hasil',methods=['POST'])
def hasil():
    pclass=int(request.form['pclass'])
    age=int(request.form['age'])
    sibsp=int(request.form['sibsp'])
    parch=int(request.form['parch'])
    sex=request.form['sex']
    fare=int(request.form['fare'])
    if sex=='male':
        male=1
        female=0
        if age>=17:
            adult_male=1
            man=1
            woman=0
            child=0
        else:
            adult_male=0
            man=0
            woman=0
            child=1
    if sex=='female':
        male=0
        female=1
        if age>=17:
            adult_male=0
            man=0
            woman=1
            child=0
        else:
            adult_male=0
            man=0
            woman=0
            child=1
    if sibsp!=0 or parch!=0:
        alone=0
    if sibsp==0 and parch==0:
        alone=1
    print(pclass,age,sibsp,parch,fare,adult_male,alone,female,male,child,man,woman)
    model=jb.load('modelTitanic')
    selamat=model.predict([[pclass,age,sibsp,parch,fare,adult_male,alone,female,male,child,man,woman]])
    data=[pclass,age,sibsp,parch,fare,adult_male,alone,female,male,child,man,woman,selamat]
    return render_template('hasil.htm',data=data)


@app.route('/postTitanic',methods=['GET','POST'])
def postTitanic():
    if request.method=='POST':
        body=request.json

        sex=body['sex']
        pclass=body['pclass']
        age=body['age']
        sibsp=body['sibsp']
        parch=body['parch']
        fare=body['fare']

        if sex=='male':
            male=1; female=0
            if age>=17:
                adult_male=1
                man=1
                woman=0
                child=0
            else:
                adult_male=0
                man=0
                woman=0
                child=1
        if sex=='female':
            male=0; female=1
            if age>=17:
                adult_male=0
                man=0
                woman=1
                child=0
            else:
                adult_male=0
                man=0
                woman=0
                child=1
        if sibsp!=0 or parch!=0:
            alone=0
        if sibsp==0 and parch==0:
            alone=1

        prediksi=int(model.predict([[pclass,age,sibsp,parch,fare,adult_male,alone,female,male,child,man,woman]])[0])

        print(type(fare))
        return jsonify({
            '0response':'POST successful!',
            'female':female,
            'male':male,
            'child':child,
            'man':man,
            'woman':woman,
            'pclass':body['pclass'],
            'age':body['age'],
            'sibsp':body['sibsp'],
            'parch':body['parch'],
            'fare':body['fare'],
            'adult_male':adult_male,
            'alone':alone,
            'zPredict':prediksi
        })

if __name__=='__main__':
    model=jb.load('modelTitanic')
    app.run(debug=True)