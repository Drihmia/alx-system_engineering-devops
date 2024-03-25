#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress in json format
saved in a file USER_ID.json.
"""
from json import dump
from requests import get
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        try:
            employee_id = int(argv[1])
        except ValueError as e:
            employee_id = "str"

        if not isinstance(employee_id, int):
            exit(0)

        # commun informations.
        usrid = f"userId={employee_id}"
        idd = f"{employee_id}"
        task_c = "completed=true"
        url = "https://jsonplaceholder.typicode.com"

        # commun informations for task 2.
        json = {f"{employee_id}": []}
        json_l = json[f"{employee_id}"]

        # getting the list of tasks
        url_full_todo = f"{url}/todos?{usrid}"
        with get(url_full_todo) as response:
            list_tasks = response.json()

        # getting the employee's username
        url_full_users_id = f"{url}/users?id={idd}"
        with get(url_full_users_id) as response:
            empl_info = response.json()
            empl_un = empl_info[0].get("username", "not found")

        for task in list_tasks:
            t_st = task.get("completed", "not found")
            title = task.get("title", "not found")
            json_l.append({"task": title,
                           "completed": t_st,
                           "username": empl_un})

        with open(f"{idd}.json", "w", encoding="utf-8") as f:
            dump(json, f)
