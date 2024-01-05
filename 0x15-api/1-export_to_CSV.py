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
