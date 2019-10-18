# -*- coding: utf8 -*-
import random #import module random
import json #import module json

def get_random_item_in(my_list):#fonction random to choise a character in my list
    rand_numb = random.randint(0, len(my_list) - 1)#rand_numb have random value between the biginin (0) and the end (len of my list)
    item = my_list[rand_numb] # get a quote from a list
    return item # return the item# get a random number
	
def read_values_from_json(file, key):
    values = []#create a list
    with open(file) as f:# open a json file with my objects
        data = json.load(f) # load all the data contained in this file f
        for entry in data:# Create a new empty list
            values.append(entry[key])# add each item in my list
    return values # return my completed list   
	
def random_character():# Return a random value from a json file
    all_values = read_values_from_json("characters.json","character")
    return get_random_item_in(all_values)
	
def random_quote():# Return a random value from a json file qotes.json
    all_values = read_values_from_json("quotes.json","quote")
    return get_random_item_in(all_values)
	
def message(character,quote): #Fonction to create the message
	return "{} a dit : {} ".format(character,quote)	
    
user_answer = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')



while user_answer != "B":# while the answer is differente to "B"
    print(message(random_character(),random_quote()))
    user_answer = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')
