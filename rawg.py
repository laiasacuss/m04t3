#!/usr/bin/env python3

import requests

api_key = "b342689533154bd4b5685d7bb828306e"
game_name = input("Introdueix un videojoc: ")

url = f"https://api.rawg.io/api/games?key={api_key}&search={game_name}&page_size=1"

response = requests.get(url)
data = response.json()

if data["results"]:
    game = data["results"][0]

    print(f"Nom: {game['name']}")
    print(f"Data llançament: {game['released']}")
    print(f"Puntuació: {game['rating']}")
    print(f"Plataformes: {[p['platform']['name'] for p in game['platforms']]}")

else:
    print("No hi han resultats")
