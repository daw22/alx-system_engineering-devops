#!/usr/bin/python3
"""
function that queries the Reddit API
"""
import requests
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """
    Retrives paginated posts of a subreddit from
    the reddit api
    """
    global after
    headers = {'User-Agent': 'myreddit'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)
