from ibm_watson import PersonalityInsightsV3
from os.path import join, dirname
import json

personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    iam_apikey='YrPs6NabVm_-02HXDJYMCVXy0cdHjclhqb0d26645lyo',
    url='https://gateway-wdc.watsonplatform.net/personality-insights/api'
)

with open(join(dirname(__file__), './profilesSmall.json')) as profile_json:
    profile = personality_insights.profile(
        profile_json.read(),
        'application/json',
        content_type='application/json',
        consumption_preferences=True,
        raw_scores=True
    ).get_result()


# print(json.dumps(profile, indent=2))

with open("output.json", "w") as file:
    json.dump(profile, file, indent=4)


listOfTraits = {}


def json_file_to_dict(input_file):
    with open(input_file, "r") as inputFile:
        data = json.load(inputFile)

    for i in data['personality']:
        listOfTraits[i['trait_id']] = i['percentile']
        for j in i['children']:
            listOfTraits[j['trait_id']] = j['percentile']

    for i in data['needs']:
        listOfTraits[i['trait_id']] = i['percentile']

    for i in data['values']:
        listOfTraits[i['trait_id']] = i['percentile']


json_file_to_dict('output.json')


print(listOfTraits)


