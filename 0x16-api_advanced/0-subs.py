#!/usr/bin/python3
"""gets the number of subscribers for a given subreddit"""

import requests
import sys

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: The number of subscribers for the subreddit if the subreddit is valid, 0 otherwise.
    """
    
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit), headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass the subreddit to be checked.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv(1))))
