# -*- coding: utf8 -*-
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]
user_answer = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')



def get_random_item_in(my_list):
    # get a random number
    item = my_list[0] # get a quote from a list
    return item # return the item



while user_answer != "B":
    print(get_random_item_in(quotes))
    user_answer = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')

for character in characters:
  n_character = character.capitalize()
  print(n_character)
print(get_random_item_in(quotes))
# show random quotes