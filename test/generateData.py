import random
import csv
# extraverted
store_extraverted = {
    "adventure": (0.8, 1.0),
    "intellect": (0.0, 0.2),
    "activity": (0.8, 1.0),
    "excitement": (0.8, 1.0),
    "outgoing": (0.8, 1.0),
    "challenge": (0.8, 1.0),
    "excitement": (0.8, 1.0),
    "charity": (0.8, 1.0),
    "music": (0.8, 1.0),
    "recreational": (0.8, 1.0),
    "social": (0.8, 1.0),
    "diy": (0.0, 0.2),
    "education": (0.0, 0.2)
}

store_introverted = {
    "adventure": (0.0, 0.2),
    "intellect": (0.8, 1.0),
    "activity": (0.0, 0.2),
    "excitement": (0.0, 0.2),
    "outgoing": (0.0, 0.2),
    "challenge": (0.0, 0.2),
    "excitement": (0.0, 0.2),
    "charity": (0.0, 0.2),
    "music": (0.0, 0.2),
    "recreational": (0.0, 0.2),
    "social": (0.0, 0.2),
    "diy": (0.8, 1.0),
    "education": (0.8, 1.0),
}

'''
1. Call the API on a block of test from reviews.csv
2. Parse response using aritra's block
[{
trait:
percentile:
}]
3. add user, trait, percentile to output.csv
4.
'''
result = []
users = []
start = 1
end = 500
mid = end // 2

for user in range(mid, end):
    for trait in store_introverted:
        users.append([user, trait, random.uniform(
            store_introverted[trait][0], store_introverted[trait][1])])
with open("output.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(users)
