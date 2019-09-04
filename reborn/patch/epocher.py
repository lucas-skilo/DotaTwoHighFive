import json
import datetime

data = {}
with open('patch.json', 'r') as json_file:
    data = json.load(json_file)
    for patch in data:
        print("got patch {} with effective begin date at {}".format(patch["name"], patch["date"]))
        epoch = datetime.datetime.strptime(patch["date"], "%Y-%m-%dT%H:00:00Z").strftime("%s")
        patch["epoch"] = int(epoch)
        print("its epoch is {}".format(epoch))

with open('patch-epoch.json', 'w') as json_file:
    json.dump(data, json_file)
