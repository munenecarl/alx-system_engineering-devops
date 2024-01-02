import requests
import json
import sys

def get_employee_todo_list(employee_id):
    # Fetch user
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user = user_response.json()

    # Fetch todos for the user
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos = todos_response.json()

    # Format todos
    user_todos = [{"task": todo["title"], "completed": todo["completed"], "username": user["name"]} for todo in todos]

    # Write to JSON file
    with open(f'{employee_id}.json', 'w') as file:
        json.dump({employee_id: user_todos}, file)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_list(employee_id)
        except ValueError:
            print("Please provide an integer as the employee ID.")
    else:
        print("Employee ID not provided.")