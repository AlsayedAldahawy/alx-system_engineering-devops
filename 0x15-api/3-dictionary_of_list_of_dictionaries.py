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
    # Import necessary modules
    from sys import argv
    import json
    import requests

    # Initialize an empty dictionary to store employee data
    dict_employees = {}

    # Initialize an empty list to store unique employee IDs
    employeesIds = []

    # Base URL for the REST API
    url = 'https://jsonplaceholder.typicode.com/'

    # Fetch user details for all employees
    users = requests.get(url + "users/").json()

    # Filter out unique employee IDs
    employeesIds = [user.get('id')
                    for user in users if user.get('id') not in employeesIds]

    # Fetch TODO list for each employee and create a dictionary entry
    for id in employeesIds:
        todos = requests.get(url + "todos/", params={'userId': id}).json()
        dict_employees[id] = [{'task': t.get('title'), 'completed': t.get(
            'completed'), 'username': users[id - 1].get('username')}
            for t in todos]

    # Write the employee data to a JSON file
    with open("todo_all_employees.json", "w") as jsonFile:
        json.dump(dict_employees, jsonFile)
