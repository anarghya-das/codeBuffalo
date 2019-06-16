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

    threshold = 0.8

                    #0          1           2      3
    categories = [education, recreation, social, diy,
                  charity, cooking, relaxation, music, busywork]
                  #4        5           6       7       8
    for trait, value in fields.items():
        print(trait, value)
        if trait == "big5_openness" and value >= threshold:
            categories[1][0] += 1
        elif trait == "facet_adventurousness" and value >= threshold:
            categories[1][0] += 1
            categories[2][0] += 1
        elif trait == "facet_artistic_interests" and value >= threshold:
            categories[3][0] += 1
            categories[7][0] += 1
        elif trait == "facet_emotionality" and value >= threshold:
            categories[6][0] += 1
            categories[4][0] += 1
        elif trait == "facet_imagination" and value >= threshold:
            categories[0][0] += 1
            categories[7][0] += 1
        elif trait == "facet_intellect" and value >= threshold:
            categories[0][0] += 1
            categories[3][0] += 1
        elif trait == "facet_liberalism" and value >= threshold:
            categories[4][0] += 1
            categories[2][0] += 1
        elif trait == "big5_conscientiousness" and value >= threshold:
            categories[8][0] += 1
            categories[0][0] += 1
            categories[4][0] += 1
        elif trait == "facet_achievement_striving" and value >= threshold:
            categories[1][0] += 1
            categories[8][0] += 1
            categories[0][0] += 1
        elif trait == "facet_cautiousness" and value >= threshold:
            pass
        elif trait == "facet_dutifulness" and value >= threshold:
            categories[0][0] += 1
            categories[8][0] += 1
            categories[4][0] += 1
        elif trait == "facet_orderliness" and value >= threshold:
            categories[0][0] += 1
            categories[3][0] += 1
        elif trait == "facet_self_discipline" and value >= threshold:
            categories[3][0] += 1
            categories[0][0] += 1
            categories[8][0] += 1
        elif trait == "facet_self_efficacy" and value >= threshold:
            categories[3][0] += 1
            categories[0][0] += 1
            categories[8][0] += 1
            categories[5][0] += 1
        elif trait == "big5_extraversion" and value >= threshold:
            categories[1][0] += 1
            categories[2][0] += 1
            categories[7][0] += 1
        elif trait == "facet_activity_level" and value >= threshold:
            categories[1][0] += 1
            categories[2][0] += 1
            categories[3][0] += 1
            categories[7][0] += 1
        elif trait == "facet_assertiveness" and value >= threshold:
            categories[2][0] += 1
            categories[7][0] += 1
        elif trait == "facet_cheerfulness" and value >= threshold:
            categories[1][0] += 1
            categories[2][0] += 1
            categories[4][0] += 1
            categories[6][0] += 1
        elif trait == "facet_excitement_seeking" and value >= threshold:
            categories[1][0] += 1
            categories[3][0] += 1
            categories[5][0] += 1
        elif trait == "facet_friendliness" and value >= threshold:
            categories[4][0] += 1
            categories[5][0] += 1
        elif trait == "facet_gregariousness" and value >= threshold:
            categories[2][0] += 1
        elif trait == "big5_agreeableness" and value >= threshold:
            categories[2][0] += 1
        elif trait == "facet_altruism" and value >= threshold:
            categories[4][0] += 1
        elif trait == "facet_cooperation" and value >= threshold:
            categories[1][0] += 1
        elif trait == "facet_modesty" and value >= threshold:
            categories[0][0] += 1
            categories[4][0] += 1
        elif trait == "facet_morality" and value >= threshold:
            categories[4][0] += 1
        elif trait == "facet_sympathy" and value >= threshold:
            categories[4][0] += 1
        elif trait == "facet_trust" and value >= threshold:
            categories[1][0] += 1
        elif trait == "big5_neuroticism" and value >= 0.7:
            categories[1][0] += 1
            categories[7][0] += 1
        elif trait == "fact_anger" and value >= 0.6:
            categories[2][0] -= 1
            categories[1][0] += 1
            categories[7][0] += 1
            categories[5][0] += 1
        elif trait == "facet_anxiety" and value >= threshold:
            categories[6][0] += 1
            categories[7][0] += 1
        elif trait == "facet_depression" and value >= threshold:
            categories[6][0] += 1
            categories[7][0] += 1
            categories[2][0] += 1
        elif trait == "facet_immoderation" and value >= threshold:
            categories[4][0] += 1
        elif trait == "facet_self_consciousness" and value >= threshold:
            categories[3][0] += 1
            categories[5][0] += 1
        elif trait == "facet_vulnerability" and value >= threshold:
            categories[6][0] += 1
            categories[7][0] += 1
        elif trait == "need_challenge" and value >= threshold:
            categories[1][0] += 1
            categories[8][0] += 1
        elif trait == "need_closeness" and value >= threshold:
            categories[4][0] += 1
            categories[7][0] += 1
        elif trait == "need_curiosity" and value >= threshold:
            categories[0][0] += 1
        elif trait == "need_excitement" and value >= threshold:
            categories[1][0] += 1
            categories[5][0] += 1
        elif trait == "need_harmony" and value >= threshold:
            categories[7][0] += 1
        elif trait == "need_idea" and value >= threshold:
            categories[0][0] += 1
            categories[3][0] += 1
        elif trait == "need_liberty" and value >= threshold:
            categories[3][0] += 1
            categories[5][0] += 1
            categories[7][0] += 1
        elif trait == "need_loove" and value >= threshold:
            categories[2][0] += 1
            categories[1][0] += 1
        elif trait == "need_practicality" and value >= threshold:
            categories[3][0] += 1
            categories[5][0] += 1
        elif trait == "need_self_expression" and value >= threshold:
            categories[7][0] += 1
            categories[3][0] += 1
        elif trait == "need_stability" and value >= threshold:
            categories[6][0] += 1
            categories[7][0] += 1
        elif trait == "need_structure" and value >= threshold:
            categories[7][0] += 1
            categories[0][0] += 1
        elif trait == "value_conservation" and value >= threshold:
            categories[5][0] += 1
            categories[4][0] += 1
        elif trait == "value_openness_to_change" and value >= threshold:
            pass
        elif trait == "value_hedonism" and value >= threshold:
            categories[3][0] += 1
            categories[7][0] += 1
            categories[2][0] += 1
        elif trait == "value_hedonism" and value >= threshold:
            categories[7][0] += 1
            categories[3][0] += 1
        elif trait == "value_self_transcendence" and value >= threshold:
            categories[0][0] += 1

    heap = list(map(tuple, categories))
    heapq.heapify(heap)
    denominator = heapq.nlargest(1, heap)[0][0]
    heap = list(map(lambda x: (x[0] / denominator, x[1]), heap))
    return heapq.nlargest(9, heap)


with open('anarghya.json') as input_file:
    content = json.load(input_file)
    dict_of_ids = {}
    for i, row in enumerate(content):
        save = row['fields']
        additional = helper(save)
        for field in additional:
            save[field[1]] = field[0]
            content[i]['fields'] = save
    with open('anarghya-categories.json', "w") as output:
        json.dump(content, output, indent = 4)
