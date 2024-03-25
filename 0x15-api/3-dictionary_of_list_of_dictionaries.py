#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress in json format
saved in a file USER_ID.json.
"""
from json import dump
from requests import get


if __name__ == "__main__":
    # commun informations.
    url = "https://jsonplaceholder.typicode.com"

    json_dict = {}

    # getting the number of users
    url_full_users = f"{url}/users"
    with get(url_full_users) as response:
        users_list = response.json()

    for usr in users_list:
        # commun informations for task 2.
        employee_id = usr.get("id", -1)
        empl_un = usr.get("username", "not found")

        json_dict.update({f"{employee_id}": []})
        json_dict_l = json_dict[f"{employee_id}"]

        # getting the list of tasks
        url_full_todo = f"{url}/todos?userId={employee_id}"
        with get(url_full_todo) as response:
            list_tasks = response.json()
            print(employee_id, len(list_tasks))

        for task in list_tasks:
            t_st = task.get("completed", "not found")
            title = task.get("title", "not found")
            json_dict_l.append({"username": empl_un, "task": title,
                           "completed": t_st})

    if json_dict:
        with open("todo_all_employees.json", "w", encoding="utf-8") as f:
            dump(json_dict, f)
