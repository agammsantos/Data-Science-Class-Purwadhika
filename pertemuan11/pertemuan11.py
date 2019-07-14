from flask import Flask, request, render_template, jsonify
app=Flask(__name__)
# request adalah untuk menyertakan cmd/data/file yg dikirimkan oleh user ke backend

@app.route('/')
def home():
    return 'Welcome!'

karyawan=[
    {'id':1,'nama':'Andi','job':'sales'},
    {'id':2,'nama':'Budi','job':'marketing'},
    {'id':3,'nama':'Caca','job':'it'}
]

# shoope.co.id/search?keyword=tamiya
@app.route('/search')
def search():
    if 'id' in request.args or 'nama' in request.args or 'job' in request.args:
        # print(request.args)
        # print(request.args['keyword'])
        # print(request.args['location'])
        if 'id' in request.args:
            id=int(request.args['id'])
            if id<1 or id>len(karyawan):
                return 'Maaf data tidak ditemukan'
            else:
                return jsonify(karyawan[id-1])
        elif 'nama' in request.args:
            i=0
            while i<len(karyawan):
                if request.args['nama'].lower() == karyawan[i]['nama'].lower():
                    # nama=str(request.args['nama'])
                    id=i
                    return jsonify(karyawan[id])
                    break
                else:
                    i+=1
                    if i==len(karyawan):
                        return 'Maaf data tidak ditemukan'
                        break
        elif 'job' in request.args:
            i=0
            while i<len(karyawan):
                if request.args['job'].lower() == karyawan[i]['job'].lower():
                    # job=str(request.args['job'])
                    id=i
                    return jsonify(karyawan[id])
                    break
                else:
                    i+=1
                    if i==len(karyawan):
                        return 'Maaf data tidak ditemukan'
                        break
            # return request.args['keyword']+' '+request.args['location']
    else:
        return 'Data tidak ditemukan'

@app.errorhandler(404)
def error():
    return render_template('error.htm')

if __name__=='__main__':
    app.run(debug=True)

# cara inisialisasi git
# git init # mengallow cmd git dalam folder
# git add . # menambahkan seluruh file dalam folder ke staging
# git add namaFile # menambahkan file ke staging
# git commit -m "blablabla" # menambahkan file/folder di staging ke repository lokal
# git log --oneline # untuk mengecek commit-commit terdahulu
# git checkout <commit id> # untuk kembali ke file commit terdahulu
# git reset <commit id> # untuk kembali ke file commit terdahulu tanpa merubah file yg telah ada sekarang dan menghapus commit setelahnya
# git reset <commit id> --hard # untuk kembali ke file commit terdahulu dengan merubah file yg telah ada sekarang dan menghapus commit setelahnya
# git remote add origin <url repository di github> # menambahkan repository online
# git push -u origin master # push commit lokal ke repository online
# git clone <url repository> # mendownload repository online ke dalam folder yg tertera di terminal
# forking di git dapat dilakukan secara manual lewat website utk mendapatkan repo user lain dalam repo sendiri