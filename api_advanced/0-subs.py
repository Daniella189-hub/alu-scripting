#!/usr/bin/python3
"""Queries the Reddit API and returns the subscriber count of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a subreddit, or 0 if invalid."""
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api_advanced:v1.0 (by /u/your_username)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False,
                                timeout=10)
        if response.status_code != 200:
            return 0
        return response.json().get("data", {}).get("subscribers", 0)
    except (requests.RequestException, ValueError):
        return 0
