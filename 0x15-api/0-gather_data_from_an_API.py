#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys

if __name__ = "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "user/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    completed = [tsk.get("title") for tsk in todos if tsk.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(i)) for i in completed]
