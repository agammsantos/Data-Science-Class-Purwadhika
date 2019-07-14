from flask import Flask, render_template, request, send_from_directory
import matplotlib.pyplot as plt
import requests
import numpy as np

app=Flask(__name__)
app.config['upload_folder']='./'

@app.route('/')
def home():
    return render_template('home.htm')

@app.route('/grafik', methods=['POST','GET'])
def grafik():
    if request.method=='POST':
        plot=request.form['plot']
        x=(request.form['x'].split(','))
        y=(request.form['y'].split(','))
        for i in x:
                if i==',':
                        x.remove(',')
        for j in y:
                if j==',':
                        y.remove(',')
        x=np.array(x).astype(int)
        y=np.array(y).astype(int)
        print(x)
        print(y)
        namagrafik=plot+'.png'
        plt.close() # untuk menutup dan menghapus saved grafik yang sudah ada 
        plt.figure('Data anda')
        plt.style.use('bmh')
        plt.plot(x,y)
        plt.xlabel('Nilai x')
        plt.ylabel('Nilai y')
        i=0
        while i<len(x):
                if i<len(x)-1:
                        if y[i]>=y[i+1]:
                                plt.text(x[i]+((max(x)-min(x))*0.01),y[i]+((max(y)-min(y))*0.01),f'({x[i]},{y[i]})') # memasukkan text di atas titik koordinat tertentu dgn posisi tergantung skala axis
                                i+=1
                        else:
                                plt.text(x[i]+((max(x)-min(x))*0.01),y[i]-((max(y)-min(y))*0.04),f'({x[i]},{y[i]})')
                                i+=1
                else:
                        plt.text(x[i]+((max(x)-min(x))*0.01),y[i]+((max(y)-min(y))*0.01),f'({x[i]},{y[i]})')
                        i+=1
        plt.xticks(np.arange(min(x)-1,max(x)+1,step=int(max(x)/len(x))))
        plt.yticks(np.arange(min(y)-1,max(y)+1,step=int(max(y)/len(y))))
        plt.minorticks_on() # menampilkan tick2 kecil
        plt.grid(True)
        plt.savefig(namagrafik)
        url='http://localhost:5000/load/'+namagrafik
        return render_template('grafik.htm',x=url)

@app.route('/load/<path:x>')
def load(x):
    return send_from_directory('./',x)


if __name__=='__main__':
    app.run(debug=True)