from pokeApi import *

# This function calls the get_all_pokemon function and returns the count of total pokemon
def get_total_pokemon_count():
    data = get_all_pokemon(0,1000)
    return data['count']