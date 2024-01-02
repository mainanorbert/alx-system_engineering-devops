#!/usr/bin/python3
"""using REST API to return TO DO LIST for given employee"""
import json
import requests
import sys


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user = '{}users/{}'.format(base_url, user_id)
    user_res = requests.get(user)
    user_obj = user_res.json()
    username = user_obj.get('username')

    todos = '{}todos?userId={}'.format(base_url, user_id)
    todo_res = requests.get(todos)
    todo_obj = todo_res.json()

    tasks = []
    for task in todo_obj:
        task_json = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": username}
        tasks.append(task_json)

    task = {str(user_id): tasks}
    filename = '{}.json'.format(user_id)
    with open(filename, 'w') as f:
        json.dump(task, f)
"""import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{base_url}/{employee_id}/todos"
    user_url = f"{base_url}/{employee_id}"

    user_data = requests.get(user_url).json()
    todo_data = requests.get(todo_url).json()
    username = user_data.get('username')

    file_name = f"{employee_id}.json"
    my_data = {employee_id: [{"task": task["title"],
                              "completed": task["completed"],
                              "username": username} for task in todo_data]}
    with open(file_name, "w") as f:
        json.dump(my_data, f)"""
