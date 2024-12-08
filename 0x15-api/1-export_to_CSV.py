#!/usr/bin/python3
"""
Script to retrieve and export to-do list information for a given employee ID.

This script fetches user and to-do list data from the JSONPlaceholder API,
and writes the to-do list information to a CSV file named after the
employee ID.

Usage:
    python script.py <employee_id>

Arguments:
    employee_id: The ID of the employee whose to-do list information will
    be retrieved.

Dependencies:
    - csv: To handle CSV file operations.
    - json: To parse JSON responses.
    - sys: To handle command-line arguments.
    - urllib.request: To make HTTP requests.

Example:
    python script.py 1
"""

import csv
import json
import sys
import urllib.request

if __name__ == "__main__":
    # Get the employee ID from command-line arguments
    employee_id = sys.argv[1]

    # Base URL of the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    with urllib.request.urlopen(f'{base_url}users/{employee_id}') as response:
        user = json.loads(response.read().decode('utf-8'))

    # Get the username of the user
    username = user.get("username")

    # Fetch to-do list information for the user
    with urllib.request.urlopen(f'{base_url}todos?userId={employee_id}') \
            as response:
        todos = json.loads(response.read().decode('utf-8'))

    # Open a CSV file to write the to-do list information
    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # Write to-do list data to the CSV file
        for todo in todos:
            writer.writerow([employee_id, username, todo.get(
                'completed'), todo.get('title')])
