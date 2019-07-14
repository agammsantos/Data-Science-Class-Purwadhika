from flask import Flask, jsonify, request
import joblib
app=Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'coef[0]':model.coef_[0],
        'coef[1]':model.coef_[1],
        'coef[2]':model.coef_[2],
        'intercept':model.intercept_
    })

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method=='POST':
        body=request.json
        prediksi=model.predict([[body['usia'],body['kamar'],body['luas']]])
        # [['usia','kamar','luas']]
        return jsonify({
            'usia':body['usia'],
            'kamar':body['kamar'],
            'luas':body['luas'],
            'status':'Anda sukses nge-POST',
            'prediksiHarga':prediksi[0]
        })
    else:
        return jsonify({
            'status':'Anda tidak nge-POST'
        })

if __name__=='__main__':
    model=joblib.load('modelPickle.pkl') # menjadi variabel global yg dapat digunakan di tiap root, joblib bisa digunakan utk mengambil file pickle
    app.run(debug=True)