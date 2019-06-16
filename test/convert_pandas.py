import pandas as pd
import json


def json_to_pandas():
    with open("anarghya.json") as file:
        final = {}
        final['trait'] = []
        final['user'] = []
        final['percentile'] = []
        content = json.load(file)
        print(content)
        for user in content:
            for field in user['fields']:
                final['user'].append(user['pk'])
                final['trait'].append(field)
                final['percentile'].append(user['fields'][field])

        return final
