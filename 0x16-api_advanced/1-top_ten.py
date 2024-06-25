#!/usr/bin/python3
"""
Refactored function to query the Reddit API and print the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API for the top ten hot posts of a given subreddit.
    Prints the titles of these posts, or None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:subreddit.topten:v1.0 (by /u/yourusername)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # This will raise an exception for HTTP error statuses
        posts = response.json().get("data", {}).get("children", [])
        
        if not posts:
            print(None)
            return

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
            else:
                print(None)
    except requests.RequestException as e:
        print(None)

# Example usage
if __name__ == "__main__":
    subreddit = "python"
    top_ten(subreddit)
