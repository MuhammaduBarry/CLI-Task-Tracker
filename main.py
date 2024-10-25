from typing import Annotated
import typer
from rich import print

from os_handler import load_json, json_file_path, dump_json, load_id

app = typer.Typer()

def current_status(status: str):
    if status == 'todo' or status == 'in-progress' or status == 'done':
        return status

@app.command()
def create_task(task: Annotated[str, typer.Argument()] = 'Task created'):
    task_info = {
        'id': load_id(),
        'description': task,
        'status': current_status('todo'),
        'created_at': None,
        'updated_at': None
    }
    print(f'task id: {task_info['id']}\n')
    print(task_info)


if __name__ == '__main__':
    app()