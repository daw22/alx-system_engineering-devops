#!/usr/bin/python3
"""
A script that prints top ten posts of a
subreddit
"""

import requests


def top_ten(subreddit):
    """
    prints top ten posts of a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    try:
        headers = {'User-Agent': """My Reddit Client /v1.0
                   (by /u/Professional-Two9987)"""}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        if len(posts) > 0:
            for post in posts:
                print(post.get("data").get("title"))
        else:
            print("None")
    except Exception as e:
        print(e)
        print("None")
