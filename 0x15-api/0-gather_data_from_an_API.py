#!/usr/bin/python3
"""
Employee TODO List Progress Checker

This Python script uses a REST API to retrieve information about
    a given employee's TODO list progress. It takes an employee ID as
        a command-line argument and fetches the following data:

1. User Information:
   - Fetches details about the employee (name, email, etc.) based on
        the provided user ID.

2. TODO List:
   - Retrieves the employee's TODO list items from the API.
   - Filters out completed tasks.

Usage:
    python employee_todo_progress.py <employee_id>

Example:
    python employee_todo_progress.py 5

Output:
    Employee John Doe is done with tasks (15/20):
        Task 1: Complete the report
        Task 2: Review project proposal
        ...
        Task 15: Send meeting agenda

Note:
- Ensure that the REST API endpoint (https://jsonplaceholder.typicode.com/)
    is accessible.
- Replace <employee_id> with the actual employee ID you want to check.
"""

if __name__ == "__main__":
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
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
                                                           len(complete),
                                                           len(todos)))
    for title in complete:
        print("\t {}".format(title))
