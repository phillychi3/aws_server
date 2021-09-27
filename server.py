from flask import Flask,request,jsonify
import base64
app = Flask(__name__)

@app.route("/")
def home():
    return "你看到我了 代表我上線了"

@app.route("/neko",methods=['GET'])
def neko():
    
    if 'name' in request.args:
        name = request.args['name']

    return "not yet lol"


@app.route("/base64",methods=['GET'])
def base():
    if 'base64' in request.args:
        base65 = request.args['base64']
    #base65=base65.encode('utf8')
    base65 = base64.b64decode(base65)
    print(base65)
    return base65


app.run()