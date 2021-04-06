from flask import Flask, request, jsonify
import json


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False



@app.route("/json", methods=["GET"])
def jsonall():
    with open("neko_data.json", "r") as jsonFile: 
        data = json.load(jsonFile) 
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
