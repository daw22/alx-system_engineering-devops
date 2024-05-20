#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""

import json
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

    dictionary = {user_id: []}
    for todo in todos:
        dictionary[user_id].append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user_name
            })
    with open("{}.json".format(user_id), "w") as f:
            json.dump(dictionary, f)
