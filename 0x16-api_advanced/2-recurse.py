#!/usr/bin/python3
"""A module that contains recurse's function"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """A function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Return: None, if:
        + an invalid subreddit is given.
        + no results are found for the given subreddit.

    Infos: The Reddit API uses pagination for separating pages of responses.
    """

    user_agent = 'MyRedditApp/1.0 by /u/Dredouane'

    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after)
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return

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
            # print(data.get("title"))
            title = data.get("title")
            if title:
                hot_list.append(title)
            else:
                return None
    # checks for 1st rwxursive call if anything has been appended to hot_list
    # +If not, means no results has been found.
    if not hot_list:
        return None

    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after=after)
