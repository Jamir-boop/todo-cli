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


#Parser
def parse(text):
    """
    Parse the given text. Returns a tuple:
    (list_of_parts, start_pos_of_the_last_part).
    """
    OUTSIDE, IN_DOUBLE, IN_SINGLE = 0, 1, 2

    iterator = enumerate(text)
    state = OUTSIDE
    parts = []
    current_part = ''
    part_start_pos = 0

    for i, c in iterator:  # XXX: correctly handle empty strings.
        if state == OUTSIDE:
            if c.isspace():
                # New part.
                if current_part:
                    parts.append(current_part)
                part_start_pos = i + 1
                current_part = ''
            elif c == '"':
                state = IN_DOUBLE
            elif c == "'":
                state = IN_SINGLE
            else:
                current_part += c

        elif state == IN_SINGLE:
            if c == "'":
                state = OUTSIDE
            elif c == "\\":
                next(iterator)
                current_part += c
            else:
                current_part += c

        elif state == IN_DOUBLE:
            if c == '"':
                state = OUTSIDE
            elif c == "\\":
                next(iterator)
                current_part += c
            else:
                current_part += c

    parts.append(current_part)
    return parts, part_start_pos