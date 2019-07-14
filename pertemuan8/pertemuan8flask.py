# pip install Flask

from flask import request, abort, Flask, render_template, jsonify

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.htm')

karyawan=[
    {'id':1,'nama':'Andi','usia':22},
    {'id':2,'nama':'Budi','usia':23},
    {'id':3,'nama':'Caca','usia':24}
]

@app.route('/data')
def data():
    return jsonify(karyawan)

@app.route('/data/<int:nomor>')
def dataSatuan(nomor):
    if nomor<1 or nomor>len(karyawan):
        abort(404)
    else:
        return jsonify(karyawan[nomor-1])

profilku={
        'nama':'Cecep Sutisna',
        'usia':21
            }
@app.route('/about')
def about():
    return render_template('about.htm',profil=profilku)

@app.route('/tes',methods=['GET','POST','PUT','DELETE'])
def tes():
    if request.method == 'GET':
        return 'Anda nge-GET'
    elif request.method == 'POST':
        pesanBody=request.json
        print(pesanBody['nama']) # print ke terminal
        return 'Pesan yg anda kirim = '+ pesanBody['nama']
    else:
        return 'Anda tidak nge-GET atau nge-POST'

@app.errorhandler(404)
def notFound(error):
    # return make_response('Maaf file tidak ditemukan') # harus digunakan import make_response
    return render_template('error.htm')

if __name__=='__main__':
    app.run(debug=True)
# untuk mengakses data yang ada dapat digunakan localhost:5000