from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://www.freetogame.com/api/games?platform=pc")
    data = response.json()[:125]

    games = []

    for game in data:
        games.append({
        'id': game['id'],
        'name': game['title'],
        'thumbnail': game['thumbnail'],
        'genre': game['genre'],
        'publisher': game['publisher']
        })

    return render_template("index.html", games=games)

@app.route("/game/<int:game_id>")
def description_link(game_id):
    response = requests.get(f"https://www.freetogame.com/api/game?id={game_id}")
    game = response.json()

    information = {
        'name': game['title'],
        'description': game['description'],
        'thumbnail': game['thumbnail'],
        'genre': game['genre'],
        'publisher': game['publisher'],
        'freetogame_profile_url': game['game_url']   #Thats what it's named in the API so keep it game_url
    }

    return render_template("information.html", information=information)

if __name__ == '__main__':
    app.run(debug=True)