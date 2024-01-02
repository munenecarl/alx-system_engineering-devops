#!/usr/bin/python3
"""Exports employees' tasks to a csv file"""

import requests
import sys
import csv

def get_employee_todo_list(employee_id):
	employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
	employee = employee_response.json()
	todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
	todos = todos_response.json()

	with open(f'{employee_id}.csv', 'w', newline='') as file:
		writer = csv.writer(file, quoting=csv.QUOTE_ALL)
		writer.writerow(["TASK_COMPLETED_STATUS", "TASK_TITLE"])
		for todo in todos:
			writer.writerow([employee_id, employee['name'], todo['completed'], todo['title']])

if __name__ == "__main__":
	if len(sys.argv) > 1:
		try:
			employee_id = int(sys.argv[1])
			get_employee_todo_list(employee_id)
		except ValueError:
			print("Please provide an integer as the employee ID.")
	else:
		print("Employee ID not provided.")
