from flask import Flask,request,jsonify
import base64
import json
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'neko api'

@app.route('/api/v1')
def apiv1():
    return 'neko api v1'

@app.route('/api/v1/neko', methods=['POST'])
def main():
    with open('nekodata.json','r') as f:
        data = json.load(f)
    neko = data[f"neko{random.randint(1,10)}"]
    return neko

app.run(port = 12345)