#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
import sys


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_id = sys.argv[1]
    full_url = base_url + "/" + user_id

    response = requests.get(full_url).json()
    user_name = response.get("name")

    todos_url = full_url + "/" + "todos"
    todos = requests.get(todos_url).json()
    completed_todos = []

    for todo in todos:
        if todo.get("completed"):
            completed_todos.append(todo)
    print("Employee {} is done with tasks({}/{})"
          .format(user_name, len(completed_todos), len(todos)))
    for todo in completed_todos:
        print("\t {}".format(todo.get("title")))
