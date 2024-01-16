#!/usr/bin/python3
"""Gets the top ten posts for a given subreddit"""

import requests
import sys

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the top ten hot posts for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Prints:
    str: The title of each hot post. If the subreddit is invalid, prints None.
    """
    
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10', headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass the subreddit to be checked.")
    else:
        print("{:d}".format(top_ten(sys.argv(1))))
