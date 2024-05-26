#!/usr/bin/python3
'''
Employee TODO List CSV Generator

This Python script fetches information about a given employee's TODO list
progress using a REST API. It takes an employee ID as a command-line argument
and performs the following steps:

1. Retrieves user details (such as username) based on the provided user ID.
2. Fetches the employee's TODO list items from the API.
3. Creates a CSV file named "<employee_id>.csv" containing the following
   columns:
   - "id": The employee ID
   - "username": The employee's username
   - "status": Whether the task is completed (True/False)
   - "title": The title of the task

Usage:
    python employee_todo_csv.py <employee_id>

Example:
    python employee_todo_csv.py 5

Output:
    Creates a CSV file named "5.csv" with relevant TODO list data.

Note:
- Ensure that the REST API endpoint (https://jsonplaceholder.typicode.com/)
    is accessible.
- Replace <employee_id> with the actual employee ID you want to check.
'''

if __name__ == "__main__":
    from sys import argv
    import csv
    import requests

    url = 'https://jsonplaceholder.typicode.com/'
    username = requests.get(url + "users/" + argv[1]).json().get('username')
    todos = requests.get(url + "todos/", params={'userId': argv[1]}).json()
    taskstatus = [t.get('completed') for t in todos]
    taskstitle = [t.get('title') for t in todos]

    with open(argv[1] + ".csv", "w") as csvFile:
        fieldnames = ["id", "username", "status", "title"]
        writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        for i, j in zip(taskstatus, taskstitle):
            writer.writerow([argv[1], username, i, j])
