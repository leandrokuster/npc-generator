import csv
import random

namesFilePath = "./resources/names.csv"
global names
family_names = []
given_names = []

class Npc:
    familyName = ""
    givenName = ""
    age = 0

    def __init__(self, givenName, familyName) -> None:
        self.givenName = givenName
        self.familyName = familyName
        pass


with open(namesFilePath, newline='') as csvfile:
    
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row)
        given_names.append(row['given_name'])
        family_names.append(row['family_name'])
        # print(row['index'], row['given_name'], row['family_name'])

    # print(given_names[random.randint(0,len(given_names)-1)])
    # print(family_names[random.randint(0,len(family_names)-1)])

    npc = Npc(given_names[random.randint(0,len(given_names)-1)], family_names[random.randint(0,len(family_names)-1)])

    print("Name: " + npc.givenName + " " + npc.familyName)


