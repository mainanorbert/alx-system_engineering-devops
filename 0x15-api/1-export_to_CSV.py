#!/usr/bin/python3
"""using REST API to return csv file for given employee details"""
import requests
import sys
import csv


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{base_url}/{employee_id}/todos"
    user_url = f"{base_url}/{employee_id}"
    user_data = requests.get(user_url).json()
    # user_id = user_data.get("id")
    username = user_data.get('username')
    todo_data = requests.get(todo_url).json()

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee_id, username, t.get("completed"), t.get("title")]
         ) for t in todo_data]
