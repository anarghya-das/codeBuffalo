from ibm_watson import PersonalityInsightsV3
import json
import sys
from os.path import join, dirname

def get_personality(text):
    personality_insights = PersonalityInsightsV3(
        version='2017-10-13',
        iam_apikey='CgEZPqJjTpxN2g90fZrjC08xJDxi954sjdmmR0eqWDxD',
        url='https://gateway-lon.watsonplatform.net/personality-insights/api'
    )

    while len(text.split()) <= 150:
        text = ' '.join((text, text))

    profile = None

    try:
        profile = personality_insights.profile(
            text,
            content_type="text/plain",
            accept="application/json"
        )
    except:
        pass

    return profile

def process_personality(data):

    listOfTraits = {}
    for i in data['personality']:
        listOfTraits[i['trait_id']] = i['percentile']
        for j in i['children']:
            listOfTraits[j['trait_id']] = j['percentile']

    for i in data['needs']:
        listOfTraits[i['trait_id']] = i['percentile']

    for i in data['values']:
        listOfTraits[i['trait_id']] = i['percentile']

    return listOfTraits
