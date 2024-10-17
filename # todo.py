# todo.py

todo_list = []

def add_task(task):
    todo_list.append(task)
    return f'Task "{task}" added!'

def view_tasks():
    if not todo_list:
        return "No tasks in your to-do list."
    return f"Your tasks: {', '.join(todo_list)}"

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        return f'Task "{task}" removed!'
    else:
        return f'Task "{task}" not found!'

# Example Usage
if __name__ == "__main__":
    print(add_task('Learn Python'))
    print(add_task('Write Code'))
    print(view_tasks())
    print(remove_task('Learn Python'))
    print(view_tasks())
