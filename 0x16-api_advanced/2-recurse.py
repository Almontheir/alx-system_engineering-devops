#!/usr/bin/python3
"""
Refactored recursive function to query the Reddit API and return a list
containing the titles of all hot articles for a given subreddit.
Returns None if no results are found for the given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=""):
    """
    Recursively queries the Reddit API for all hot articles of a given subreddit
    and compiles their titles into a list. Returns None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:subreddit.recursive:v1.0 (by /u/yourusername)"}
    params = {"after": after}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()

        posts = data.get("data", {}).get("children", [])
        after = data.get("data", {}).get("after")

        for post in posts:
            title = post.get("data", {}).get("title")
            hot_list.append(title)

        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list if hot_list else None
    except requests.RequestException:
        return None

# Example usage
if __name__ == "__main__":
    subreddit = "python"
    titles = recurse(subreddit)
    if titles:
        for title in titles:
            print(title)
    else:
        print(None)
