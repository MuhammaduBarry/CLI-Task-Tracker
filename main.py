from typing import Annotated
import typer
from rich import print
from rich.console import Console
from rich.table import Table
from os_handler import *
import datetime

app = typer.Typer()
console = Console()
status = ['todo', 'in-progress', 'done']

@app.command()
def add(task: Annotated[str, typer.Argument()] = 'Task created'):
    """Create new task and saves it to JSON file"""
    task_info = {
        'id': increment_id_number(),
        'description': task,
        'status': status[0],
        'created_at': str(datetime.datetime.now())[:16],
        'updated_at': None
    }
    data = load_json(json_file_path)
    data["list_of_task"].append(task_info)
    dump_json(json_file_path, data)

@app.command()
def current_status():
    """Create a table that display current status"""
    data = load_json(json_file_path)
    table = Table('ID', 'DESCRIPTION', 'STATUS', 'CREATED-AT', 'UPDATED-AT')
    for task in data['list_of_task']:
        table.add_row(
            str(task['id']),
            task['description'],
            task['status'],
            task['created_at'],
            task['updated_at']
        )
    console.print(table)


@app.command()
def update(id_number: int, new_task: str):
    """Update an existing task"""
    data = load_json(json_file_path)

    if len(data["list_of_task"]) == 0 :
        print('doesnt exist yet, create one')

    for information in data["list_of_task"]:
        if information["id"] == id_number:
            information["description"] = new_task
            information["updated_at"] = str(datetime.datetime.now())[:16]

    dump_json(json_file_path, data)


@app.command()
def delete(id_number: int):
    """Delete an existing task"""
    data = load_json(json_file_path)

    if len(data["list_of_task"]) == 0 :
        print('doesnt exist yet, create one')

    for task in data["list_of_task"]:
        if task["id"] == id_number:
            data["list_of_task"].remove(task)
            print("Running delete task.....")
    data["amount_of_task"] -= 1
    dump_json(json_file_path, data)

def mark(id_number: int, index: int):
    """Template for mark-in-progress & mark-done"""
    data = load_json(json_file_path)
    for task in data["list_of_task"]:
        if task["id"] == id_number:
            task["status"] = status[index]
    dump_json(json_file_path, data)

@app.command()
def mark_in_progress(id_number: int):
    """Change task state to in-progress"""
    mark(id_number, 1)

@app.command()
def mark_done(id_number: int):
    """Change task state to done"""
    mark(id_number, 2)

def show(index: int):
    """Template to filter status"""
    data = load_json(json_file_path)
    table = Table('ID', 'DESCRIPTION', 'STATUS', 'CREATED-AT', 'UPDATED-AT')
    for task in data["list_of_task"]:
        if task["status"] == status[index]:
            table.add_row(
                str(task['id']),
                task['description'],
                task['status'],
                task['created_at'],
                task['updated_at']
            )
            console.print(table)
    dump_json(json_file_path, data)

@app.command()
def show_done():
    """Display table to state 'done'"""
    show(2)

@app.command()
def show_todo():
    """Display table to state 'todo'"""
    show(0)

@app.command()
def show_in_progress():
    """Display table to state 'in-progress'"""
    show(1)

if __name__ == '__main__':
    app()