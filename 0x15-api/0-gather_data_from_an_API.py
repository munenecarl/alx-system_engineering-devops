"""Gathers data from the fake data API"""

import requests
import sys

def get_employee_todo_list(employee_id):
	"""Fetches employee data"""
	employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
	employee = employee_response.json()
	todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
	todos = todos_response.json()
	total_tasks = len(todos)
	done_tasks = len([todo for todo in todos if todo['completed']])
	print(f"Employee {employee['name']} is done with tasks({done_tasks}/{total_tasks}):")
	for todo in todos:
		if todo['completed']:
			print(f"\t {todo['title']}")

if __name__ == "__main__":
	if len(sys.argv) > 1:
		try:
			employee_id = int(sys.argv[1])
			get_employee_todo_list(employee_id)
		except ValueError:
			print("Please provide an integer as the employee ID.")
	else:
		print("Employee ID not provided.")