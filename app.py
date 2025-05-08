from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://api.disneyapi.dev/character")
    data = response.json()
    print(data)
