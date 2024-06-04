#!/usr/bin/python3
"""
A script to get number of subscribers of a subreddit
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """
    Queries Reddit api and returns the number of
    subscribers for a given subredit
    Args:
        subreddit: name of the subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        response = requests.get(url, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except requests.exceptions.RequestException as e:
        return 0
