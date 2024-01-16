#!/usr/bin/python3
"""Queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit."""

import requests
import sys

def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.
    hot_list (list, optional): A list of titles of hot articles. Defaults to an empty list.
    after (str, optional): The ID of the last post in the previous page. Defaults to None.

    Returns:
    list: A list of titles of hot articles if the subreddit is valid, None otherwise.
    """

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
