#!/usr/bin/python3
"""recurse"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """returns a list of titles of all hot articles for a given subreddit"""
    if hot_list is None:
        return None
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/124.0.0.0 Safari/537.36'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for post in data:
            hot_list.append(post.get('data').get('title'))

        after = response.json().get('data').get('after')
        if after:
            return recurse(subreddit, hot_list, after)

        return hot_list
    else:
        return None
