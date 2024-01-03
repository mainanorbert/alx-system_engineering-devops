#!/usr/bin/python3
"""
The module uses REST API for employee ID
and return information TODO list progress
"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(base_url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, task.get("completed"), task.get("title")]
         ) for task in todos]
"""if __name__ == '__main__':
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
        tasks.append([user_id,
                      username,
                      task.get('completed'),
                      task.get('title')])

    filename = '{}.csv'.format(user_id)
    with open(filename, 'w') as f:
        data = csv.writer(f, delimiter=',',
                          quotechar='"',
                          quoting=csv.QUOTE_ALL)

        for task in tasks:
            data.writerow(task)"""
