#!/usr/bin/python3
"""using RESR API to return TO DO LIST for given employee"""
import requests
import sys
import json


def employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{base_url}/{employee_id}/todos"
    user_url = f"{base_url}/{employee_id}"
    
    # fetching user data
    user_data = requests.get(user_url).json()
    
    # fetching user todo work
    todo_data = requests.get(todo_url).json()
    
    file_name = f"{employee_id}.json"
    my_data = {employee_id: [{"task": task["title"], "completed": task["completed"], "username": task["username"]} for task in todo_data]}
    with open(file_name, m="w") as f:
        json.dump(my_data, f)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employee_todo_progress(employee_id)
