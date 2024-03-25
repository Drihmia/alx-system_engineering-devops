#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress in csv format
saved in a file USER_ID.csv.
"""
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

        # getting Number of tasks
        url_full_todo = f"{url}/todos?{usrid}"
        with get(url_full_todo) as response:
            list_tasks = response.json()

        # getting the employee's username
        url_full = f"{url}/users?id={idd}"
        with get(url_full) as response:
            empl_info = response.json()
            empl_un = empl_info[0].get("username", "not found")

        csv_format = ""
        for task in list_tasks:
            t_st = task.get("completed", "not found")
            title = task.get("title", "not found")
            csv_format += f"\"{idd}\",\"{empl_un}\",\"{t_st}\",\"{title}\"\n"

        with open(f"{idd}.csv", "w", encoding="utf-8") as f:
            f.write(csv_format[:-1])
