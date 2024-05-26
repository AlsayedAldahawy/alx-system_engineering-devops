#!/usr/bin/python3
'''
Employee TODO List JSON Generator

This Python script fetches information about a given employee's TODO list
progress using a REST API. It takes an employee ID as a command-line argument
and performs the following steps:

1. Retrieves user details (such as username) based on the provided user ID.
2. Fetches the employee's TODO list items from the API.
3. Creates a JSON file named "<employee_id>.json" containing a dictionary with
   the following structure:
   {
       "<employee_id>": [
           {
               "task": "Task title",
               "completed": true/false,
               "username": "Employee username"
           },
           ...
       ]
   }

Usage:
    python employee_todo_json.py <employee_id>

Example:
    python employee_todo_json.py 5

Output:
    Creates a JSON file named "5.json" with relevant TODO list data.

Note:
- Ensure that the REST API endpoint (https://jsonplaceholder.typicode.com/)
  is accessible.
- Replace <employee_id> with the actual employee ID you want to check.
'''

if __name__ == "__main__":
    from sys import argv
    import json
    import requests

    url = 'https://jsonplaceholder.typicode.com/'
    username = requests.get(url + "users/" + argv[1]).json().get('username')
    todos = requests.get(url + "todos/", params={'userId': argv[1]}).json()
    tasks = [{'task': t.get('title'), 'completed': t.get(
        'completed'), 'username': username} for t in todos]

    with open(argv[1] + ".json", "w") as jsonFile:
        json.dump({argv[1]: tasks}, jsonFile)
