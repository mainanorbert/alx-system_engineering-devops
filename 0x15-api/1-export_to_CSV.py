#!/usr/bin/python3
"""using RESR API to return TO DO LIST for given employee"""
import requests
import sys
import csv


def employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{base_url}/{employee_id}/todos"
    user_url = f"{base_url}/{employee_id}"
    user_data = requests.get(user_url).json()
    employee_name = user_data.get("name")
    user_id = user_data.get("id")
    username = user_data.get('username')
    todo_data = requests.get(todo_url).json()

    file_name = f"{user_id}.csv"
    with open(file_name, mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            writer.writerow([user_id, username, task.get('completed'),
                            task.get('title')])


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employee_todo_progress(employee_id)
