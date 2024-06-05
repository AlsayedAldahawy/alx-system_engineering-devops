#!/usr/bin/python3
"""top ten"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/124.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for post in data[:10]:
            print(post.get('data').get('title'))
    else:
        return None
