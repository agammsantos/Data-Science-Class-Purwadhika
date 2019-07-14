from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('soal5.htm')

@app.route('/aboutme')
def about():
    return render_template('tentangsaya.htm')

@app.route('/faq')
def faq():
    return render_template('faq.htm')

@app.route('/contact')
def contact():
    return render_template('contact.htm')

if __name__=='__main__':
    app.run(debug=True)