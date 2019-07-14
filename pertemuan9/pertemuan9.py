from flask import Flask, send_from_directory, render_template, request, redirect, url_for
app=Flask(__name__)

# home route
@app.route('/')
def home():
    return '<h1>Welcome to my web server</h1>'

# render static file => localhost:5000/images/PNG_transparency_demonstration_2.png
@app.route('/images/<path:x>')
def staticfile(x):
    return send_from_directory('images',x) # nama folder dinyatakan disini atau agar root tidak perlu msk folder lg bisa diganti 'images/foto'

@app.route('/html')
def html():
    return render_template('html.htm')

# ngePOST dari html dan menampilkan datanya
@app.route('/post', methods=['POST'])
def post():
    name=request.form['nama']
    pswd=request.form['pass']
    print('Nama:',name,'Password:',pswd)
    return redirect(url_for('profil',nama=name)) # menuju route dimana didefinisikan endpoint profil dgn argumen nama=name
    # ngePOST dari postman dan mengambil datanya
    # data=request.json
    # print('Anda nge-POST: '+data['nama']+' '+data['pass'])
    # return 'Anda nge-POST: '+ data['nama']+' '+data['pass']

@app.route('/<string:nama>')
def profil(nama):
    return '<h1>Selamat datang '+nama+'</h1>'

# 404 route
@app.errorhandler(404)
def error404(error):
    return '<h1>Error: 404 Not Found</h1>'

if __name__=='__main__':
    app.run(debug=True)
