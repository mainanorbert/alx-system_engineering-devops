#!/usr/bin//python3
"""Recording all tasks from all employees"""

import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{base_url}/users").json()
    with open("todo_all_employees.json", "w") as f:
        json.dump({
            user.get("id"): [{
                "task": task.get("title"),
                "complete": task.get("completed"),
                "username": user.get("username")
            } for task in requests.get(
                                       f"{base_url}/todos",
                                       params={
                                           "userId": user.get("id")}).json()]
            for user in users}, f)
