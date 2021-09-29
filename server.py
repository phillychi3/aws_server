from flask import Flask,request,jsonify
import base64
import requests as rq
app = Flask(__name__)

@app.route("/")
def home():
    return "你看到我了 代表我上線了"

@app.route("/neko")
def neko():
    
    r = rq.get("127.0.0.1:12345/api/v1/neko")

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


app.run()