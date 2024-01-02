#!/usr/bin/python3
"""exports the tasks of all employees in json format"""

import json
import requests

def get_all_employees_todo_list():
	""" Fetch all tasks for all users"""
	users_response = requests.get('https://jsonplaceholder.typicode.com/users')
	users = users_response.json()

	all_todos = {}

	for user in users:
		todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user["id"]}')
		todos = todos_response.json()
		user_todos = [{"username": user["name"], "task": todo["title"], "completed": todo["completed"]} for todo in todos]
		all_todos[user["id"]] = user_todos
	with open('todo_all_employees.json', 'w') as file:
		json.dump(all_todos, file)

if __name__ == "__main__":
	get_all_employees_todo_list()
