#!/usr/bin/python3
"""
exports data in the CSV format
"""


import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_id = sys.argv[1]
    full_url = base_url + "/" + user_id

    response = requests.get(full_url).json()
    user_name = response.get("username")

    todos_url = full_url + "/" + "todos"
    todos = requests.get(todos_url).json()
    completed_todos = []

    for todo in todos:
        if todo.get("completed"):
            completed_todos.append(todo)
    with open("{}.csv".format(user_id), "w") as csv:
        for todo in todos:
            csv.write('"{}","{}","{}","{}"\n'
                      .format(user_id, user_name,
                              todo.get("completed"),
                              todo.get("title")))
