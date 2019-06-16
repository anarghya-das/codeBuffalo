import pandas as pd
import json

#Eventually wanna load the json from graphQL

def json_to_pandas():
    with open("anarghya-categories.json") as file:
        final = {}
        final['trait'] = []
        final['user'] = []
        final['percentile'] = []
        content = json.load(file)
        for user in content:
            for field in user['fields']:
                final['user'].append(user['pk'])
                final['trait'].append(field)
                final['percentile'].append(user['fields'][field])

        return final
