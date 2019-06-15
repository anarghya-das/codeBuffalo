import csv
from ibm_watson import PersonalityInsightsV3
from os.path import join, dirname
import json


def get_personality(text):
    # aritra's code + API call
    personality_insights = PersonalityInsightsV3(
        version='2017-10-13',
        iam_apikey='YrPs6NabVm_-02HXDJYMCVXy0cdHjclhqb0d26645lyo',
        url='https://gateway-wdc.watsonplatform.net/personality-insights/api'
    )

    while len(text.split()) <= 100:
        print("length issue")
        text = ' '.join((text, text))
    data = {}
    data['contentItems'] = [
        {"content": text,
         "contenttype": "text/plain",
         "language": "en"}
    ]
    with open("profileTemp.json", "w") as file:
        json.dump(data, file)

    with open(join(dirname(__file__), './profileTemp.json')) as profile_json:
        profile = personality_insights.profile(
            profile_json.read(),
            'application/json',
            content_type='application/json',
            consumption_preferences=True,
            raw_scores=True
        ).get_result()

        listOfTraits = {}

        for i in profile['personality']:
            listOfTraits[i['trait_id']] = i['percentile']
            for j in i['children']:
                listOfTraits[j['trait_id']] = j['percentile']

        for i in profile['needs']:
            listOfTraits[i['trait_id']] = i['percentile']

        for i in profile['values']:
            listOfTraits[i['trait_id']] = i['percentile']

        return listOfTraits


def get_text(row):
    return (int(row[0]), row[-1])


def write_output(personalities):
    print(personalities)
    users = []
    for user in personalities:
        for trait in personalities[user]:
            users.append([user, trait, personalities[user][trait]])
    with open("output.csv", "w+") as file:
        writer = csv.writer(file)
        writer.writerows(users)


def main():
    reader = None
    content = []
    with open('Reviews.csv') as file:
        import pdb
        pdb.set_trace()
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i <= 40:
                continue
            content.append(get_text(row))
    personalities = {}
    for i, user in enumerate(content):
        personalities[user[0]] = get_personality(user[1])

        # personalities = [(id, {trait1: score, trait2: score ......}}]
        write_output(personalities)


main()
