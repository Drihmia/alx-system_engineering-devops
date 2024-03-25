#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
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
            n_tasks = len(list_tasks)
            # print("TOTAL_NUMBER_OF_TASKS", n_tasks)

        # getting Number of finished tasks
        url_full_todo = f"{url}/todos?{usrid}"
        url_full_todo = f"{url}/todos?{usrid}&{task_c}"
        with get(url_full_todo) as response:
            list_tasks_finished = response.json()
            # number of finished tasks
            n_tasks_f = len(list_tasks_finished)
            # print("NUMBER_OF_DONE_TASKS", n_tasks_f)

        # getting the employee's name
        url_full = f"{url}/users?id={idd}"
        with get(url_full) as response:
            empl_info = response.json()
            empl_n = empl_info[0].get("name", "not found")
            # print("EMPLOYEE_NAME", empl_n)

        print(f"Employee {empl_n} is done with tasks({n_tasks_f}/{n_tasks}):")
        for task in list_tasks_finished:
            print("\t", task.get("title", "not found"))
