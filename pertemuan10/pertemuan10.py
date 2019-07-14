from flask import Flask, render_template, url_for, request, send_from_directory
from werkzeug.utils import secure_filename
import os
app=Flask(__name__)
app.config['upload_folder']='storage'

# home route
@app.route('/')
def home():
    return render_template('home.htm')

# bootstrap and upload route
@app.route('/new')
def new():
    return render_template('new.htm')

@app.route('/upload', methods=['POST'])
def upload():
    data=request.files['filesaya']
    namafile=secure_filename(data.filename)
    namafile='1.jpg'
    data.save(os.path.join(app.config['upload_folder'],namafile))
    print(data)
    return 'Anda ngupload' and send_from_directory('storage',namafile)
#   return redirect('/storage/'+namafile) # alternatif cara

# @app.route('/storage/<path:x>')
# def suksesUpload(x):
#   return send_from_directory('storage',x)

# 404 error handler
@app.errorhandler(404)
def notFound404(error):
    return render_template('error.htm')

if __name__=='__main__':
    app.run(debug=True)