from flask import Flask
from flask import Response
#from flask_ngrok import run_with_ngrok #hanya digunakan ketika menggunakan google colab dan tidak untuk di deploy ke heroku
import json

f1 = open('./convective_map.geojson')
f2 = open('./cape_map.geojson')
f3 = open('./li_map.geojson')
f4 = open('./ki_map.geojson')

geodata1 = json.load(f1)
geodata2 = json.load(f2)
geodata3 = json.load(f3)
geodata4 = json.load(f4)

pelatihan_ibf_app = Flask(__name__)
#run_with_ngrok(pelatihan_ibf_app) #hanya digunakan ketika menggunakan google colab dan tidak untuk di deploy ke heroku  

@pelatihan_ibf_app.route('/')
def send_json_data():
    return {
  "about": "Cuaca di Kalimantan", 
  "authors": [
    {
      "name": "Ahmad Rifani", 
      "division": "PPC - BMKG"
    },{
      "name": "Muhammad Hakiki", 
      "division": "PPC - BMKG"
    },{
      "name": "Adinda Dara Vahada", 
      "division": "PCS - BMKG"
      }
  ]
}
    
@pelatihan_ibf_app.route('/convective/')
def send_json_convective():
    return Response(response=json.dumps(geodata1),
                    status=200,
                    mimetype="application/json")
    
@pelatihan_ibf_app.route('/cape')
def send_json_cape():
    return Response(response=json.dumps(geodata2),
                    status=200,
                    mimetype="application/json")
    
@pelatihan_ibf_app.route('/li')
def send_json_li():
    return Response(response=json.dumps(geodata3),
                    status=200,
                    mimetype="application/json")

@pelatihan_ibf_app.route('/ki')
def send_json_ki():
    return Response(response=json.dumps(geodata4),
                    status=200,
                    mimetype="application/json")
    
if __name__ == '__main__':
    pelatihan_ibf_app.run()