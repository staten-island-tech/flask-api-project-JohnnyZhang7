from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://mhw-db.com/monsters")
    data = response.json()

    monsters = []
    for monster in data:
        monsters.append({
            'id': monster['id'],
            'name': monster['name'],
            'image': monster.get('image', '')
        }) 
    return render_template("index.html", monsters=monsters)

@app.route("/monster/<monster_id>")
def monster_detail(monster_id):
    response = requests.get(f"https://mhw-db.com/monsters/{monster_id}")
    monster = response.json()

    monster_details = {
        'name': monster.get('name'),
        'image': monster.get('image'),
        'description': monster.get('description', 'No description available'),
        'weaknesses': monster.get('weaknesses', []),
        'habitats': monster.get('habitats', []),
    }
    return render_template("monster_detail.html", monster=monster_details)

if __name__ == "__main__":
    app.run(debug=True)
