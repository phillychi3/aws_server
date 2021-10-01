from flask import Flask,request,jsonify
import base64
import requests as rq
import random
app = Flask(__name__)

@app.route("/")
def home():
    return "你看到我了 代表我上線了"

@app.route("/neko",methods=['GET'])
def neko():
    if 'nekomame' in request.args:
        name = request.args['nekomame']
    data = {"data":{name}}
    r = rq.post("http://127.0.0.1:12345/api/v1/neko",data=data)
    text = r.text
    return text

@app.route("/base64",methods=['GET'])
def base():
    if 'base64' in request.args:
        base65 = request.args['base64']
    #base65=base65.encode('utf8')
    base65 = base64.b64decode(base65)
    print(base65)
    return base65

app.run(port=80,path="0.0.0.0")