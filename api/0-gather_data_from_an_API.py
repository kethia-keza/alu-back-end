#!/usr/bin/python3
"""Returns information about a/an employee's TODO list progress."""

if __name__ == "__main__":
    try:
        import requests
        import sys

        employee_id = int(sys.argv[1])
        base_url = "https://jsonplaceholder.typicode.com"
        user = requests.get(
            "{}/users/{}".format(base_url, employee_id), timeout=10).json()
        todos = requests.get(
            "{}/todos?userId={}".format(base_url, employee_id),
            timeout=10).json()
        done = [t.get("title") for t in todos if t.get("completed")]
        print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(done), len(todos)))
        for title in done:
            print("\t {}".format(title))
    except Exception as e:
        print("ERROR: {}".format(repr(e)))
