#!/usr/bin/python3
'''
Employee TODO List Progress Checker
'''

# Import necessary modules
import requests
from sys import argv

# Base URL for the REST API
url = "https://jsonplaceholder.typicode.com/"

# Fetch user information based on the provided user ID
user = requests.get(url + "users/" + argv[1]).json()

# Fetch TODO list for the same user
todos = requests.get(url + "todos", params={'userId': argv[1]}).json()

# Filter completed tasks
complete = [c.get("title") for c in todos if c.get('completed') is True]

# Print summary of completed tasks
print("Employee {} is done with tasks ({}/{}):".format(user.get('name'),
                                                       len(complete),
                                                       len(todos)))
for title in complete:
    print("\t{}".format(title))
