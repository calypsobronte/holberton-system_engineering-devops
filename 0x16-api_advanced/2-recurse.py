#!/usr/bin/python3
"""API reddit """
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = 'https://www.reddit.com/r/{}/hot.json?\
           after={}'.format(subreddit, after)
    headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;\
                         rv:68.0) Gecko/20100101 FirefoxFirefox/68.0'}
    with requests.session() as client:
        info = client.get(url, headers=headers, allow_redirects=False).json()
        try:
            for i in info.get('data').get('children'):
                hot_list.append(i.get("data").get("title"))
            return hot_list + recurse(subreddit, [],
                                      info.get("data").get("after"))
        except Exception:
            if after is None:
                return []
