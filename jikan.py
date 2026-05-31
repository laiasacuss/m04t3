#!/usr/bin/env python3

import requests 

anime_name = input("Introdueix un anime: ") 

url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1" 

response = requests.get(url) 
data = response.json()

if data["data"]: 
    anime = data["data"][0]

    print(f"Títol: {anime['title']}")
    print(f"Epsiodis: {anime['episodes']}") 
    print(f"Puntuació: {anime['score']}")
    print(f"Any: {anime['year']}")
    print(f"URL: {anime['url']}") 

    print(anime['synopsis']) 

else:
    print("No he trobat resultats") 
