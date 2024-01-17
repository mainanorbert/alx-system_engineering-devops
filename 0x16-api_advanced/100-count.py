#!/usr/bin/python3
""""modeule the returns list of titles of all hot articles"""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "Ubuntu 22.04.2 LTS"}

    params = {"after": after, "limit": 100}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    after = data.get("after")
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()

        for keyword in word_list:
            keyword_lower = keyword.lower()
            if keyword_lower in title:
                count_dict[keyword_lower] = count_dict.get(keyword_lower,
                                                           0) + 1

    if after:
        count_words(subreddit, word_list, after, count_dict)
    else:
        """print_results(count_dict)"""
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print(f"{keyword}: {count}")
