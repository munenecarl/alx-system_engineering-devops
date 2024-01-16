#!/usr/bin/env python3

import requests
import sys

def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-Agent': 'my-app/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after:
        url += f'?after={after}'
    
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()['data']
    hot_list.extend(post['data']['title'] for post in data['children'])

    if data['after'] is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, data['after'])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass the subreddit to be checked.")
    else:
        print("{:d}".format(recurse(sys.argv(1))))
