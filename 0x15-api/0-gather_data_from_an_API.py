#!/usr/bin/python3
'''
Python script that, using REST API, for a given employee ID
returns information about his/her TODO list progress.
'''

if __name__ == "__main__":

    import requests
    from sys import argv

    argc = len(argv)
    user_id = argv[1]
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    compleated_tasks = []

    url = "https://jsonplaceholder.typicode.com/users/" + user_id
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        EMPLOYEE_NAME = data.get('name')
        print(data.get('name'))
    else:
        print(f"Error: {response.status_code}")

    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # Parse JSON response

        for i in data:
            if i.get('userId') == int(argv[1]):
                TOTAL_NUMBER_OF_TASKS += 1
                if i.get('completed'):
                    NUMBER_OF_DONE_TASKS += 1
                    compleated_tasks.append(i.get('title'))

        print("Employee {} is done with tasks({}/{})".format(EMPLOYEE_NAME,
              NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
        for i in compleated_tasks:
            print("\t", i)

    else:
        print(f"Error: {response.status_code}")
