# make API call to GET https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0

import requests

# This function calls the get_all_pokemon function and returns the response from API request
# using default function params incase caller doesn't provide any
def get_all_pokemon(limit=1000, offset=0):
    url = f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}'
    response = requests.get(url)
    data = response.json()
    return data