#!/usr/bin/python3
"""A module that contains top_ten's function"""

import requests


def top_ten(subreddit):
    """A function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.

    print: None, If an invalid subreddit is given.
    """

    user_agent = 'MyRedditApp/1.0 by /u/Dredouane'

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)
    json = r.json()

    # getting the main data of the Listing.
    main_data = json.get("data")
    children = main_data.get("children")

    count = 0
    for child in children:
        # I've noticed that even when I set limit to 10 i get 3 extra titles.
        # +so i ve limited it manually with the count variable.
        if count >= 10:
            break
        count += 1
        # getting the data.
        data = child.get("data")

        if data.get("subreddit_id").startswith("t5"):
            print(data.get("title"))
        else:
            print("None")
