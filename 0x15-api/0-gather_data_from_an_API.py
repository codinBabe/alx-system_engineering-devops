#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    # the url endpoint
    url = "https://jsonplaceholder.typicode.com/"

    # get request for user info
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()

    # get request for todo list
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # check for completed todo list
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # print employee name, completed tasks & total no of tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # print the titles of completed task with indentation
    [print("\t {}".format(i)) for i in completed]
