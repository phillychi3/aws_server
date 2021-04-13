from flask import Flask, request, jsonify
import json
import logging

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False
count=0

FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, filename='myLog.log',encoding='utf-8', filemode='w', format=FORMAT)

@app.route("/neko", methods=["GET"])
def jsonall():
    with open("neko_data.json", "r") as jsonFile: 
        data = json.load(jsonFile)
        global count
        count+=1
        logging.info(f"目前次數:{count}")
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
