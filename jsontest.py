import json


with open('game.json', "r") as f: 
    data = json.load(f)
    
data["games"].append({"game":2})
print(data)


with open('game.json', "w") as f: 
    data = json.dump(data, f, indent=4)