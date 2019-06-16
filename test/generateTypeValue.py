import json
import heapq


def helper(fields):
    heap = []
    social = [0, "social"]
    education = [0, "education"]
    recreation = [0, "recreation"]
    diy = [0, "diy"]
    charity = [0, "charity"]
    cooking = [0, "cooking"]
    relaxation = [0, "relaxation"]
    music = [0, "music"]
    busywork = [0, "busywork"]

    categories = [education, recreation, social, diy, charity, cooking, relaxation, music, busywork]

    for trait, value in fields.items():
        print(trait, value)
        if trait == "big5_openness" and value >= 0.8:
            categories[1][0] += 1
        elif trait == "facet_adventurousness" and value >= 0.8:
            categories[1][0] += 1
        elif trait == "facet_artistic_interests" and value >= 0.8:
            categories[3][0] += 1
        elif trait == "facet_emotionality" and value >= 0.8:
            categories[6][0] += 1
        elif trait == "facet_imagination" and value >= 0.8:
            categories[0][0] += 1
        elif trait == "facet_intellect" and value >= 0.8:
            categories[0][0] += 1
        elif trait == "facet_liberalism" and value >= 0.8:
            categories[4][0] += 1
            categories[2][0] += 1
        elif trait == "big5_conscientiousness" and value >= 0.8:
            categories[8][0] += 1
            categories[0][0] += 1
        elif trait == "facet_achievement_striving" and value >= 0.8:
            categories[1][0] += 1
            categories[8][0] += 1
        elif trait == "facet_cautiousness" and value >= 0.8:
            categories[8][0] += 1
        elif trait == "facet_dutifulness" and value >= 0.8:
            categories[0][0] += 1
            categories[8][0] += 1
        elif trait == "facet_orderliness" and value >= 0.8:
            categories[1][0] += 1
            categories[8][0] += 1
        elif trait == "facet_self_discipline" and value >= 0.8:
            categories[3][0] += 1
            categories[7][0] += 1
        elif trait == "facet_self_efficacy" and value >= 0.8:
            categories[5][0] += 1
            categories[4][0] += 1
        elif trait == "big5_extraversion" and value >= 0.8:
            categories[1][0] += 1
            categories[2][0] += 1
            categories[4][0] += 1
        elif trait == "facet_activity_level" and value >= 0.8:
            categories[1][0] += 1
            categories[2][0] += 1
            categories[3][0] += 1
            categories[5][0] += 1
        elif trait == "facet_assertiveness" and value >= 0.8:
            categories[2][0] += 1
            categories[4][0] += 1
            categories[7][0] += 1
        elif trait == "facet_cheerfulness" and value >= 0.8:
            categories[1][0] += 1
            categories[2][0] += 1
        elif trait == "facet_excitement_seeking" and value >= 0.8:
            categories[1][0] += 1
            categories[3][0] += 1
            categories[5][0] += 1
        elif trait == "facet_friendliness" and value >= 0.8:
            categories[4][0] += 1
            categories[5][0] += 1
        elif trait == "facet_gregariousness" and value >= 0.8:
            categories[2][0] += 1
        elif trait == "big5_agreeableness" and value >= 0.8:
            categories[2][0] += 1
        elif trait == "facet_altruism" and value >= 0.8:
            categories[4][0] += 1
        elif trait == "facet_cooperation" and value >= 0.8:
            categories[1][0] += 1
        elif trait == "facet_modesty" and value >= 0.8:
            categories[0][0] += 1
            categories[4][0] += 1
        elif trait == "facet_morality" and value >= 0.8:
            categories[4][0] += 1
        elif trait == "facet_sympathy" and value >= 0.8:
            categories[4][0] += 1
        elif trait == "facet_trust" and value >= 0.8:
            categories[1][0] += 1
        elif trait == "big5_neuroticism" and value >= 0.7:
            categories[1][0] += 1
            categories[7][0] += 1
        elif trait == "fact_anger" and value >= 0.6:
            categories[2][0] -= 1
            categories[1][0] += 1
            categories[7][0] += 1
            categories[5][0] += 1
        elif trait == "facet_anxiety" and value >= 0.8:
            categories[6][0] += 1
            categories[7][0] += 1
        elif trait == "facet_depression" and value >= 0.8:
            categories[6][0] += 1
            categories[7][0] += 1
            categories[2][0] += 1
        elif trait == "facet_immoderation" and value >= 0.8:
            categories[4][0] += 1
        elif trait == "facet_self_consciousness" and value >= 0.8:
            categories[3][0] += 1
            categories[5][0] += 1
        elif trait == "facet_vulnerability" and value >= 0.8:
            categories[6][0] += 1
            categories[7][0] +=1
        elif trait == "need_challenge" and value >= 0.8:
            categories[1][0] += 1
            categories[8][0] += 1
        elif trait == "need_closeness" and value >= 0.8:
            categories[4][0] += 1
            categories[7][0] += 1
        elif trait == "need_curiosity" and value >= 0.8:
            categories[0][0] += 1
        elif trait == "need_excitement" and value >= 0.8:
            categories[1][0] += 1
            categories[5][0] += 1
        elif trait == "need_harmony" and value >= 0.8:
            categories[7][0] += 1
        elif trait == "need_idea" and value >= 0.8:
            categories[0][0] += 1
            categories[3][0] += 1
        elif trait == "need_liberty" and value >= 0.8:
            categories[3][0] += 1
            categories[5][0] += 1
            categories[7][0] += 1
        elif trait == "need_loove" and value >= 0.8:
            categories[2][0] += 1
            categories[1][0] += 1
        elif trait == "need_practicality" and value >= 0.8:
            categories[3][0] += 1
            categories[5][0]+= 1
        elif trait == "need_self_expression" and value >= 0.8:
            categories[7][0] += 1
            categories[3][0] += 1
        elif trait == "need_stability" and value >= 0.8:
            categories[6][0] += 1
            recreation[7][0] += 1
        elif trait == "need_structure" and value >= 0.8:
            categories[7][0] += 1
            categories[0][0] += 1
        elif trait == "value_conservation" and value >= 0.8:
            categories[5][0] += 1
            categories[4][0] += 1
        elif trait == "value_openness_to_change" and value >= 0.8:
            pass
        elif trait == "value_hedonism" and value >= 0.8:
            categories[3][0] += 1
            categories[7][0] += 1
            categories[2][0] += 1
        elif trait == "value_hedonism" and value >= 0.8:
            categories[7][0] += 1
            categories[3][0] += 1
        elif trait == "value_self_transcendence" and value >= 0.8:
            categories[0][0] += 1

    #for j in categories:
    #    heapq.heappush(heap, (j[0], j[1]))
    #categories = list(map(lambda x: (-x[0], x[1]), categories))
    heap = list(map(tuple, categories))
    heapq.heapify(heap)
    denominator = heapq.nlargest(1, heap)[0][0]
    heap = list(map(lambda x: (x[0]/denominator, x[1]), heap))
    print(heapq.nlargest(9, heap))


with open('anarghya.json') as input_file:
    content = json.load(input_file)
    dict_of_ids = {}
    for i, row in enumerate(content, start=1):
        save = row['fields']
        helper(save)
        break



