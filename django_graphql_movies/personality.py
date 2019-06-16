from get_personality import *
from recommender import run_model
from bored import get_activity

#text = input("How do you feel today? (100 words or more): ")
# text = " The kind of blasphemy you people run really makes me sick, I mean really sick. For instance in your February 28 issue, right on page 14, your interviewer asks Lily Tomlin, \"Who's the funniest person you ever met?\" and she answers right away, without batting an eye, \"Oh, God.\" Well I don't believe Lily Tomlin ever met God. And I don't believe God is funny. You're sick, that's all I can say. Really really sick."
# 1. Input goes to server
# 2. Server queries IBM for insights
# 3. Server receives JSON of traits
# 4. Server runs SVD based on the new traits
# 5. Server gets rating of activity categories based on the derived personality
# 6. Pick top n and query BoredAPI for activities in those n categories, or further filter based on no. of participants


def get_activities(text):

    personality = get_personality(text)

    if not personality:
        # TODO: Use default text
        pass

    personality = process_personality(personality.result)

    predicted_categories = run_model(personality)
    activities = get_activity([category[1]
                               for category in predicted_categories])

    return activities
