#!/usr/bin/env python 3

import requests
from collections import Counter
import re
import sys

def count_words(subreddit, word_list, counts=None, after=None):
    if counts is None:
        counts = Counter()

    headers = {'User-Agent': 'my-app/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass the subreddit to be checked.")
    else:
        print("{:d}".format(count_words(sys.argv(1), [x for x in sys.argv[2].split()])))
