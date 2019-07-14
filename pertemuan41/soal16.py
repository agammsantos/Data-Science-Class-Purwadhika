from flask import Flask, request, render_template
import requests
import joblib as jb

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.htm')

@app.route('/hasil',methods=['POST'])
def hasil():
    pclass=int(request.form['pclass'])
    age=int(request.form['age'])
    sibsp=int(request.form['sibsp'])
    parch=int(request.form['parch'])
    sex=request.form['sex']
    fare=int(request.form['fare'])
    metode=request.form['metode']
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
    modeltree=jb.load('treeTitanic')
    selamattree=modeltree.predict([[pclass,age,sibsp,parch,fare,adult_male,alone,female,male,child,man,woman]])
    if metode=='Logistic Regression':
        if selamat[0]==1:
            return 'Anda selamat!'
        elif selamat[0]==0:
            return 'Anda tewas!'
    elif metode=='Decision Tree':
        if selamattree[0]==1:
            return 'Anda selamat!'
        elif selamattree[0]==0:
            return 'Anda tewas!'
    elif metode=='All':
        if selamat[0]==1 and selamattree[0]==1:
            return 'Menurut LogReg, Anda selamat!<br>Menurut DecTree, Anda juga selamat!'
        elif selamat[0]==0 and selamattree[0]==1:
            return 'Menurut LogReg, Anda tewas!<br>Menurut DecTree, Anda selamat!'
        elif selamat[0]==1 and selamattree[0]==0:
            return 'Menurut LogReg, Anda selamat!<br>Menurut DecTree, Anda tewas!'
        else:
            return 'Menurut kedua metode, Anda pasti tewas!'

if __name__=='__main__':
    app.run(debug=True)