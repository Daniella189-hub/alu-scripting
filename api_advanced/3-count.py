#!/usr/bin/python3
"""Recursively counts keywords in the titles of hot posts of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print sorted keyword counts from hot post titles."""
    if counts is None:
        counts = {}
        for word in word_list:
            w = word.lower()
            counts[w] = counts.get(w, 0)

    if not subreddit or not isinstance(subreddit, str):
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api_advanced:v1.0 (by /u/your_username)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return

    # Number of times each distinct keyword appears in the word_list
    # (duplicates in word_list multiply the count, e.g. 'JavA java' -> x2)
    multiplier = {}
    for word in word_list:
        w = word.lower()
        multiplier[w] = multiplier.get(w, 0) + 1

    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for token in title.lower().split():
            if token in multiplier:
                counts[token] += multiplier[token]

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, after, counts)

    results = [(w, c) for w, c in counts.items() if c > 0]
    results.sort(key=lambda x: (-x[1], x[0]))
    for word, count in results:
        print("{}: {}".format(word, count))
