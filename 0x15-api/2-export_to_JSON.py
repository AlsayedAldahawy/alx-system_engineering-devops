#!/usr/bin/python3

import json
import urllib.request
import sys

'''
    Python script to export data in the JSON format.
'''
if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    response = urllib.request.urlopen(url + f"users/{id}")
    user_name = json.loads(response.read()).get("username")

    response = urllib.request.urlopen(url + f"todos?userName={id}")
    todos = json.loads(response.read())

    user_tasks = [{"task": t.get("title"), "completed": t.get(
        "completed"), "username": user_name} for t in todos]

    with open(f"{id}.json", mode="w") as file:
        json.dump({id: user_tasks}, file)
