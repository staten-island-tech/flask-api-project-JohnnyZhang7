def divide(a,b):
    try:
        #try something
        result = a/b
    except ZeroDivisionError:
        print("Error cannot divide by 0")
    else:
        print(result)
divide(10,0)

import requests

response = requests.get("https://www.freetogame.com/api/games?platform=pc")
data = response.json()

number_of_games = len(data)
print(f"There are {number_of_games} games in the response.")
