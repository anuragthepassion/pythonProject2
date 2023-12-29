FILEPATH = 'venv/bin/Files/todo.txt'
#functionvenv/bin/Files/todo.txt
def get_todos(filepath=FILEPATH):
    """
    Get todoes
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
