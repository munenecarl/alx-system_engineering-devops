#!/usr/bin/python 3
"""Queries the Reddit API, parses the title of all hot articles, and counts occurrences of given keywords."""

import requests
from collections import Counter
import re
import sys

def count_words(subreddit, word_list, counts=None, after=None):
    """
    Queries the Reddit API, parses the title of all hot articles, and counts occurrences of given keywords.

    Parameters:
    subreddit (str): The name of the subreddit to query.
    word_list (list): A list of keywords to count.
    counts (Counter, optional): A Counter dictionary for keyword counts. Defaults to a new Counter if not supplied.
    after (str, optional): The ID of the last post in the previous page. Defaults to None.

    Returns:
    None. The function prints a sorted count of the keywords in descending order by count and then alphabetically.
    If no posts match or the subreddit is invalid, prints nothing.
    """

    if counts is None:
        counts = Counter()

    headers = {'User-Agent': 'my-app/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += f'?after={after}'

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()['data']
    for post in data['children']:
        title = post['data']['title'].lower()
        words = re.findall(r'\b\w+\b', title)
        for word in words:
            if word in word_list:
                counts[word] += 1

    if data['after'] is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f'{word}: {count}')
    else:
        count_words(subreddit, word_list, counts, data['after'])

