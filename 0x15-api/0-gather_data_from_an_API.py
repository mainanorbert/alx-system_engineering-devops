#!/usr/bin/python3
"""using RESR API to return TO DO LIST for given employee"""
import requests
import sys


def employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{base_url}/{employee_id}/todos"
    user_url = f"{base_url}/{employee_id}"
    user_data = requests.get(user_url).json()
    employee_name = user_data.get("name")
    todo_data = requests.get(todo_url).json()
    total_tasks = len(todo_data)
    completed_tasks = sum(task["completed"] for task in todo_data)
    print(f"Employee {employee_name} is \
          done with tasks({completed_tasks}/{total_tasks}): ")
    for task in todo_data:
        if task["completed"]:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employee_todo_progress(employee_id)
