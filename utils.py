import json

class TODO:
	def import_todo():
		f = open('todo.json')
		return json.load(f)

	def close_todo():
		import_todo()

# CRUD FILES 
def add_task(DATA, task):
	DATA["tasks"] = task
