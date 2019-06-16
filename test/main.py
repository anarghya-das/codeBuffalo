from get_personality import *
from recommender import run_model

text = input("How do you feel today? (100 words or more): ")

# 1. Input goes to server
# 2. Server queries IBM for insights
# 3. Server receives JSON of traits
# 4. Server runs SVD based on the new traits
# 5. Server gets rating of activity categories based on the derived personality
# 6. Pick top n and query BoredAPI for activities in those n categories, or further filter based on no. of participants


personality = get_personality(text)

if not personality:
    #TODO: Use default text
    pass

personality = process_personality(personality.result)

predicted_categories = run_model(personality)
print(predicted_categories)
