#!/usr/bin/python3
"""
Refactored function to query the Reddit API and return the number of subscribers
for a given subreddit. Returns 0 for an invalid subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for a given subreddit and returns the number of subscribers.
    Returns 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # This will raise an exception for 4XX and 5XX status codes
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except requests.RequestException:  # Catches any request-related errors
        return 0

# Example usage
if __name__ == "__main__":
    subreddit = "python"
    print(f"Subscribers in /r/{subreddit}: {number_of_subscribers(subreddit)}"
