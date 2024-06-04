from flask import Flask, request, jsonify
import pandas as pd
from model import * 

app = Flask(__name__)
df_data = pd.read_csv("/Users/jonathansantos/Desktop/IronHack/Projectofinalop/data/raw/data.csv")

@app.route('/', methods=['POST'])  # added POST method
def index():
    # recover JSON with the request
    data = request.get_json()  # use get_json() to parse the JSON request data
    # Return JSON response
    return { "recomendation": recommend_songs(data['songs'], df_data)}

app.run()

