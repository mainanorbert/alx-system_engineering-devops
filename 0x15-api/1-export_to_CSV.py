#!/usr/bin/python3
"""
script that uses REST API, for a given employee ID,
exports the data to csv file.
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """ main function """
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user = f"{url}/users/{id}"
    todo = f"{url}/todos?userId={id}"

    employee = requests.get(user).json()
    tasks = requests.get(todo).json()

    name = employee['name']
    uname = employee['username']
    # total = len(tasks)
    # done = [task for task in tasks if task['completed']]

    filename = f"{id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            status = "True" if task['completed'] else "False"
            csv_writer.writerow([id, uname, status, task['title']])
