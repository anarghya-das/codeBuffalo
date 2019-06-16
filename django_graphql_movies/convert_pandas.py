import pandas as pd
import json
import requests
#Eventually wanna load the json from graphQL

load_local = True

def json_to_pandas():

    final = {}
    final['trait'] = []
    final['user'] = []
    final['percentile'] = []
    if load_local:
        file = open("store.json")
        content = json.load(file)
        for user in content:
            for field in user['fields']:
                final['user'].append(user['pk'])
                final['trait'].append(field)
                final['percentile'].append(user['fields'][field])
        file.close()
        return final

    url = "https://codebuffalohack.appspot.com/graphql/"
    params = {"query": "{ users { id big5Openness facetAdventurousness facetArtisticInterests facetEmotionality facetImagination facetIntellect facetLiberalism big5Conscientiousness facetAchievementStriving facetCautiousness facetDutifulness facetOrderliness facetSelfDiscipline facetSelfEfficacy big5Extraversion facetActivityLevel facetAssertiveness facetCheerfulness facetExcitementSeeking facetFriendliness facetGregariousness big5Agreeableness facetAltruism facetCooperation facetModesty facetMorality facetSympathy facetTrust big5Neuroticism facetAnger facetAnxiety facetDepression facetImmoderation facetSelfConsciousness facetVulnerability needChallenge needCloseness needCuriosity needExcitement needHarmony needIdeal needLiberty needLove needPracticality needSelfExpression needStability needStructure valueConservation valueOpennessToChange valueHedonism valueSelfEnhancement valueSelfTranscendence } }"}
    count = 0
    while True:
        try:
            content = requests.post(url, params).json()
            break
        except:
            count += 1
            print("Error: trying again")
            break
    for user in content['data']['users']:
        for field in user:
            if field == 'id':
                continue
            final['user'].append(user['id'])
            final['trait'].append(field)
            final['percentile'].append(user[field])
    return final
