#!/usr/bin/python3
"""
functionn that queries the Reddit API
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Queries the reddit api for the number of subscrbers
    a given subreddit have
    """
    headers = {'User-Agent': 'myreddit'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
