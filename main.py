from typing import Annotated
import typer
from rich import print
from rich.console import Console
from rich.table import Table
from os_handler import *
import datetime

app = typer.Typer()
console = Console()

def current_state(status: str):
    if status in ['todo', 'in-progress', 'done']:
        return status

@app.command()
def add(task: Annotated[str, typer.Argument()] = 'Task created'):
    task_info = {
        'id': increment_id_number(),
        'description': task,
        'status': current_state('todo'),
        'created_at': str(datetime.datetime.now())[:16],
        'updated_at': None
    }
    load(task_info)

@app.command()
def current_status():
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
    data = load_json(json_file_path)
    if len(data["list_of_task"]) == 0 :
        print('doesnt exist yet, create one')
    for information in data["list_of_task"]:
        if information["id"] == id_number:
            information["description"] = new_task
    dump_json(json_file_path, data)



@app.command()
def delete():
    pass

@app.command()
def update_current_status():
    pass

if __name__ == '__main__':
    app()