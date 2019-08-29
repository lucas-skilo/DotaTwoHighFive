import json

with open('heroes.json', 'r') as json_file:
    heroes = json.load(json_file)
    i = 1
    for hero in heroes:
        print("found {} heroes!".format(i))
        i +=1