#!/usr/bin/python3
"""
Script to retrieve and display to-do list information for a given employee ID.

This script fetches user and to-do list data from the JSONPlaceholder API and prints
the completed tasks for a specific user.

Usage:
    python script.py <employee_id>

Arguments:
    employee_id: The ID of the employee whose to-do list information will be retrieved.
"""

import json
import urllib.request
import sys

def fetch_json_data(url):
    """
    Fetch JSON data from the provided URL.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        dict: The JSON data as a dictionary.
    """
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode('utf-8'))

if __name__ == "__main__":
    # Get the employee ID from command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    
    # Base URL of the JSONPlaceholder API
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Fetch user information
    user_url = f"{base_url}users/{employee_id}"
    user = fetch_json_data(user_url)

    # Fetch to-do list information for the user
    todos_url = f"{base_url}todos?userId={employee_id}"
    todos = fetch_json_data(todos_url)

    # Extract titles of completed tasks
    completed_tasks = [task.get("title") for task in todos if task.get("completed")]

    # Print user and completed tasks information
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task))
