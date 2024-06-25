#!/usr/bin/python3
"""
Refactored function to count words in all hot posts of a given Reddit subreddit.
"""

import requests

def count_words(subreddit, word_list):
    """
    Function to count words in all hot posts of a given Reddit subreddit.
    Prints a sorted count of given keywords.
    """
    if not word_list or not subreddit:
        return

    counts = {}
    headers = {"User-Agent": "python:subreddit.wordcounter:v1.0 (by /u/yourusername)"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100}
    
    try:
        while True:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raises an HTTPError for unsuccessful status codes

            data = response.json()
            children = data.get("data", {}).get("children", [])
            
            for post in children:
                title = post.get("data", {}).get("title", "").lower()
                for word in word_list:
                    if word.lower() in title:
                        counts[word] = counts.get(word, 0) + title.count(word.lower())
            
            after = data.get("data", {}).get("after")
            if after:
                params["after"] = after
            else:
                break
        
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
    
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    subreddit = "python"
    words_to_count = ["python", "reddit", "function"]
    count_words(subreddit, words_to_count)
