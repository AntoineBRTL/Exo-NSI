import json

def getJSON(path):
    f = open(path)
    j = json.load(f)
    f.close()
    return j

config = getJSON("config.json")

print(config["mode"] + " " + config["nom"])