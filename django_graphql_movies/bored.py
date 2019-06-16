import requests

def get_activity(categories):
    activities = []
    for category in categories:
        activities.append((requests.get("http://www.boredapi.com/api/activity", params={"type": category})).json()['activity'])
    return activities
