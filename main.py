
# import json
# from pydoc import describe

# f = open('tasks.json')
# data = json.load(f)

# tasks = []

# class task:
#     def __init__(self, name, description, state):
#         self.name = name
#         self.description = description
#         self.state = state


# for data in data["tasks"]:
#     name = data["name"]
#     description = data["description"]
#     state = data["state"]
#     tasks.append(task(name, description, state))



from prompt_toolkit.buffer import Buffer

buffer1 = Buffer(
    name = "Percy"
)

print(buffer1.name)