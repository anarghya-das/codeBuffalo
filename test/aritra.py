import csv
import pprint
import collections
import json

with open("output.csv") as file:
    reader = csv.reader(file)
    result = []
    anarghya = collections.defaultdict(lambda: (int, dict))
    for row in reader:
        _id = int(row[0])
        if _id not in anarghya:
            anarghya[_id] = {}
        anarghya[_id][row[1]] = float(row[2])
    for user in anarghya:
        u = {}
        u["model"] = "movies.users"
        u["pk"] = user
        u["fields"] = anarghya[user]
        result.append(u)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(result)
    with open("anarghya.json", "w") as anarghya:
        json.dump(result, anarghya, indent = 4)

