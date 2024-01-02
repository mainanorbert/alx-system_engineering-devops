#!/usr/bin//python3
"""Recording all tasks from all employees and saves to json file"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{base_url}/users").json()
    with open("todo_all_employees.json", "w") as f:
        json.dump({
            user.get("id"): [{
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed"),
            } for task in requests.get(
                                       f"{base_url}/todos",
                                       params={
                                           "userId": user.get("id")}).json()]
            for user in users}, f)
