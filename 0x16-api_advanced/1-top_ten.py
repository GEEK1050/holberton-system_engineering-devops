#!/usr/bin/python3
"""0-subs.py"""
import requests


def number_of_subscribers(subreddit):
    """return top post of subscribers
       reddit"""
    h = {'user-agent': 'GEEK1050'}
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(link, headers=h)

    req_data = req.json().get("data").get("subscribers")
    for element in req_data['children']:
        print(element['children']['title'])
