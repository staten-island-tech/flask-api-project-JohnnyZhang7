from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():

    response = requests.get("https://ghibliapi.vercel.app/api/films")
    films = response.json()

    return render_template("index.html", films=films)

@app.route("/film/<film_id>")
def film_detail(film_id):
    response = requests.get(f"https://ghibliapi.vercel.app/api/films/{film_id}")
    film = response.json()

    return render_template("film.html", film=film)

if __name__ == "__main__":
    app.run(debug=True)