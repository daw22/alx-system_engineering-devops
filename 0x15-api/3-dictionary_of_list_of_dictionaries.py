#!/usr/bin/python3
"""
fetches all todos of all emploeeys and
export data in the JSON format
"""


import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"

    users_todos = {}
    users = requests.get(base_url).json()
    for user in users:
        users_todos[user.get("id")] = []
        url_user = base_url + "/" + str(user.get("id")) + "/" + "todos"
        user_todos_list = requests.get(url_user).json()
        for todo in user_todos_list:
            users_todos[user.get("id")].append({
                "username": user.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed")
                })

    with open("todo_all_employees.json", "w") as f:
        json.dump(users_todos, f)
