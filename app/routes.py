from app import app
from flask import render_template, request, jsonify
import requests
import os, ssl


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/add_message', methods=['POST'])
def add_message():
    cardnumber = request.form['cardnumber']
    exdate = request.form['exdate']
    cvv = request.form['cvv']
    #res1 = requests.post("https://tntnyon7yop.SANDBOX.verygoodproxy.com/post",
    #                    json={'cardnumber': cardnumber, 'exdate': exdate, "cvv": cvv})
    return render_template('message.html', cardnumber=cardnumber, exdate=exdate, cvv=cvv)

@app.route("/forward", methods=['POST'])
def forward():
    cardnumber = request.form['cardnumber']
    exdate = request.form['exdate']
    cvv = request.form['cvv']

    os.environ['HTTPS_PROXY'] = 'https://USbPuC36M68eFxyZL889bUr5:f576d63a-5376-41e4-ae91-a43e2e723822@tntnyon7yop.SANDBOX.verygoodproxy.com:8080'
    res = requests.post("https://echo.apps.verygood.systems/post",
                        json={"cardnumber": cardnumber, "exdate": exdate, "cvv": cvv},
                        verify='C:/Users/Kat/Desktop/simple_app_test_vgs/app/cert.pem')
    res = res.json() 
    return render_template('forward.html', response=res)
