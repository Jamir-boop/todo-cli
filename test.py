# import json
# TODO = "todo.json"

# with open(TODO, "r+") as file:
#     input = {
#         "id":"4",
#         "description": "nikhil@geeksforgeeks.org",
#         "state": "incomplete"
#     }
    
#     DATA = json.load(file)
#     DATA["tasks"].append(input)
#     file.seek(0)
#     json.dump(DATA, file, indent=4)

# from prompt_toolkit import prompt
# from prompt_toolkit import print_formatted_text
# from prompt_toolkit.formatted_text import ANSI, HTML, FormattedText
# from prompt_toolkit.styles import Style
# print = print_formatted_text
# def  hello():
# 	name = prompt('What is your name?: ')
# 	style = Style.from_dict({"hello": "#fb1222", "name": "#14afb4 italic",})
# 	text_fragments = FormattedText(
# [("class:hello", "Hello "), ("class:name", name), ("", "\n"),]
# )
# 	print(text_fragments, style=style)
# if  __name__ == "__main__":
# 	hello()


# def parse(text):
#     """
#     Parse the given text. Returns a tuple:
#     (list_of_parts, start_pos_of_the_last_part).
#     """
#     OUTSIDE, IN_DOUBLE, IN_SINGLE = 0, 1, 2

#     iterator = enumerate(text)
#     state = OUTSIDE
#     parts = []
#     current_part = ''
#     part_start_pos = 0

#     for i, c in iterator:  # XXX: correctly handle empty strings.
#         if state == OUTSIDE:
#             if c.isspace():
#                 # New part.
#                 if current_part:
#                     parts.append(current_part)
#                 part_start_pos = i + 1
#                 current_part = ''
#             elif c == '"':
#                 state = IN_DOUBLE
#             elif c == "'":
#                 state = IN_SINGLE
#             else:
#                 current_part += c

#         elif state == IN_SINGLE:
#             if c == "'":
#                 state = OUTSIDE
#             elif c == "\\":
#                 next(iterator)
#                 current_part += c
#             else:
#                 current_part += c

#         elif state == IN_DOUBLE:
#             if c == '"':
#                 state = OUTSIDE
#             elif c == "\\":
#                 next(iterator)
#                 current_part += c
#             else:
#                 current_part += c

#     parts.append(current_part)
#     return parts, part_start_pos


# text = "Mi mama me mima cuando voy a la fiesta"

# print(parse(text))



# import argparse
# if  __name__ == "__main__":
# 	parser = argparse.ArgumentParser(description="""
# 	Let us create a user contact.""")
# 	parser.add_argument("name", help="Name of the user")
# 	parser.add_argument("password", help="Password")
# 	parser.add_argument("email", help="Email")
# 	args = parser.parse_args()
# 	name_v = args.name
# 	password_v = args.password
# 	email_v = args.email
# 	print("Name : " + name_v)
# 	print("Password : " + password_v)
# 	print("Email : " + email_v)




import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-d')
args = parser.parse_args()
print(getattr(args,args.name))