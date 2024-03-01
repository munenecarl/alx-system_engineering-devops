#!/usr/bin/python3
"""Module to print the top 10 hot posts of a subreddit"""

import requests


def top_ten(subreddit):
    """Prints the top 10 hot posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers).json()

    if response.get("error") == 404:
        print("None")
        return 0
    for post in response.get("data").get("children"):
        print(post.get("data").get("title"))
