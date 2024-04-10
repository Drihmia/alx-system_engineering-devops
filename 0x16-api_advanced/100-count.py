#!/usr/bin/python3
"""A module that contains count_words's function"""

import requests


def count_words(subreddit, word_list, after=None, word_dict={}):
    """A function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Return: None, if:
        + an invalid subreddit is given.
        + no results are found for the given subreddit.

    Infos: The Reddit API uses pagination for separating pages of responses.
    """

    user_agent = 'MyRedditApp/1.0 by /u/Dredouane'

    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return

    word_list = (([word.lower() for word in word_list]))
    if not word_dict:
        word_dict = {word: 0 for word in word_list}

    json = r.json()

    # getting the main data of the Listing.
    main_data = json.get("data")
    after = main_data.get("after")

    children = main_data.get("children")
    if not len(children):
        return None

    for child in children:
        # I've noticed that even when I set limit to 10 i get 3 extra titles.
        # +so i ve limited it manually with the count variable.
        # getting the data.
        data = child.get("data")

        if data.get("subreddit_id").startswith("t5"):
            title = data.get("title")
            if title:
                for word in word_dict:
                    title = title.lower()
                    title_list = title.split()
                    if word in title_list:
                        word_dict[word] += title_list.count(word)
    if not after:
        for word, count in word_dict.items():
            print("{}:".format(word), count)
        return word_dict

    return count_words(subreddit, word_list, after=after, word_dict=word_dict)
