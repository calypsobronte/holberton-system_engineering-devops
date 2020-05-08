#!/usr/bin/python3
"""API reddit """
import requests


def recurse(subreddit, hot_list=[], after=''):
    url = 'https://www.reddit.com/r/{}/hot.json?\
           after={}'.format(subreddit, after)
    headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;\
                         rv:68.0) Gecko/20100101 FirefoxFirefox/68.0'}
    try:
        info = requests.get(url, headers=headers, allow_redirects=False).json()
        child = info.get('data').get('children')
        after = info.get('data').get('after')
        for i in child:
            hot_list.append(i.get('data').get('title'))
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except Exception:
        return None
