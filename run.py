from flask import Flask
#from flask_ngrok import run_with_ngrok #hanya digunakan ketika menggunakan google colab dan tidak untuk di deploy ke heroku
from flask import request
from flask import Response
from flask_cors import CORS
import json
import copy

geo = {
  "type": "FeatureCollection",
  "features": []
}

pelatihan_ibf_app = Flask(__name__)
CORS(pelatihan_ibf_app)
#run_with_ngrok(pelatihan_ibf_app) #hanya digunakan ketika menggunakan google colab dan tidak untuk di deploy ke heroku  

@pelatihan_ibf_app.route('/impact', methods=["GET"])
def send_status():
    req = json.loads(request.data)
    return Response(response=json.dumps(geo),
                    status=200,
                    mimetype="application/json")

@pelatihan_ibf_app.route('/impact/add', methods=["POST"])
def add_status():
    req = json.loads(request.data)
    for a in req["features"]:
      geo["features"].append(copy.copy(req[a]))
    
    return Response(response=json.dumps(geo),
                    status=200,
                    mimetype="application/json")

if __name__ == '__main__':
    pelatihan_ibf_app.run()