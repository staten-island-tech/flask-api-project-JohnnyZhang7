from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get("https://random-d.uk/api/v2/duck?count=100")
    data = response.json()
    duck_urls = data.get('urls', [])

    ducks = []

    for i, url in enumerate(duck_urls, start=1):    #This one gives random images unlike the pokemon one so i need this
        ducks.append({
            'name': f"Duck {i}",
            'id': i,
            'image': url
        })

    return render_template("index.html", ducks=ducks)

if __name__ == '__main__':
    app.run(debug=True)