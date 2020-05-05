#!/usr/bin/python3
""" API employee ID """

import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    api_todos = requests.get(url_todos.format(user_id)).json()
    url_names = 'https://jsonplaceholder.typicode.com/users/{}'
    name_users = requests.get(url_names.format(user_id)).json()
    list_tasks = [task.get('title') for task in api_todos
                  if task.get('completed')]
    print("Employee {} is done with tasks({}/{}):"
          .format(name_users.get('name'), len(list_tasks), len(api_todos)))
    [print("\t {}".format(task)) for task in list_tasks]
