#!/usr/bin/python3
""" API employee ID """

import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    api_todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)).json()
    name_users = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()
    list_tasks = [task.get('title') for task in api_todos if task.get('completed')]
    print("Employee {} is done with tasks({}/{}):".format(name_users.get('name'), len(list_tasks), len(api_todos)))
    [print("\t {}".format(task)) for task in list_tasks]
