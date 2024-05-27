#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
to returns info about employee TODO progress
"""
import re
import requests
import sys


API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_resp = requests.get('{}/users/{}'.format(API, id)).json()
            todos_resp = requests.get('{}/todos'.format(API)).json()
            user_name = user_resp.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todos_resp))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(todos_done),
                    len(todos)
                )
            )
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))
