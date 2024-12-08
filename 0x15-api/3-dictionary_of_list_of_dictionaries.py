#!/usr/bin/python3


"""
extend your Python script to export data in the JSON format.
"""

import json
import urllib.request

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    response = urllib.request.urlopen(url + "users")
    users = json.loads(response.read())

    response = urllib.request.urlopen(url + "todos")
    todos = json.loads(response.read())

    resu = [{user.get("id"): [{"username": user.get("username"),
                               "task": todo.get("title"),
                               "completed": todo.get("completed")}
                              for todo in todos
                              if todo.get("userId") == user.get("id")]}
            for user in users]

    print(*resu)
