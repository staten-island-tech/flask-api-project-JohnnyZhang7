from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://www.freetogame.com/api/games?platform=pc")
    data = response.json()   #My API doesn't have ?limit as a parameter, there are only 339 games

    genres = []
    genre_groups = {}

    for game in data:

        if game['genre'] not in genres:
            genres.append(game['genre'])    #Stores the individual genres so that I can sort them later
            genre_groups[game['genre']] = []
        game_info = {
            'id': game['id'],
            'name': game['title'],
            'thumbnail': game['thumbnail'],
            'genre': game['genre'],
            'publisher': game['publisher']
        }
        genre_groups[game['genre']].append(game_info)



    return render_template("index.html", genre_groups=genre_groups)


@app.route("/game/<int:game_id>")
def description_link(game_id):
    response = requests.get(f"https://www.freetogame.com/api/game?id={game_id}")
    game = response.json()
    try:
        information = {
        #'chaojie' : game['chaojie'],    #If I add chaojie into the information, it isn't part of the API so returns with an error
        'name': game['title'],
        'description': game['description'],
        'thumbnail': game['thumbnail'],
        'genre': game['genre'],
        'publisher': game['publisher'],
        'freetogame_profile_url': game['freetogame_profile_url']   #Thats what it's named in the API so you have to put it in information.html too
    }
    except KeyError:
        print("Error: Key not found")
    else:
        return render_template("information.html", information=information)
    

if __name__ == '__main__':
    app.run(debug=True)