#!/usr/bin/python3
"""Exports employees' tasks to a csv file"""

import csv
import requests
import sys

def get_employee_todo_list(employee_id):
	employee_response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
				  .format(employee_id))
	employee = employee_response.json()
	todos_response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
			       .format(employee_id))
	todos = todos_response.json()

	with open("{}.csv"
	   .format(employee_id), 'w', newline='') as file:
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
