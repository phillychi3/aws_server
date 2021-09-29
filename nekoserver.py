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
    num = request.form.get('data')
    neko = data[f"neko{num}"]
    return neko


"""neko APi v2, /api/v2/upload when user upload image -> save image 
    /api/v2/neko when user request it , returns a neko image""" #<- my bad english lol
#測試用    
# @app.route('/api/v2/upload', methods=['POST'])
# def upload():
#     # get image from request
#     img = request.files.get('img')
#     # save image
#     img.save(f'{random.randint(1,1000)}.png')
#     return 'upload success'



app.run(port = 12345)