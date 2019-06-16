from ibm_watson import PersonalityInsightsV3
from os.path import join, dirname
import json
import csv

personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    iam_apikey='YrPs6NabVm_-02HXDJYMCVXy0cdHjclhqb0d26645lyo',
    url='https://gateway-wdc.watsonplatform.net/personality-insights/api'
)

with open(join(dirname(__file__), './twitter.json')) as profile_json:
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
list_of_music_genre = {}


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


def music_genre_score(input_file):
    with open(input_file, "r") as inputFile:
        data = json.load(inputFile)

    for i in data['consumption_preferences']:
        if i['consumption_preference_category_id'] == "consumption_preferences_music":
            for j in i['consumption_preferences']:
                list_of_music_genre[j["consumption_preference_id"][29:]] = j['score']


music_genre_score("activities.json")

with open('people1.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(list_of_music_genre)

csvFile.close()
print(list_of_music_genre)
