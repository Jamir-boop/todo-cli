import json

def import_file(dir):
	f = open(dir)
	return json.load(f)
