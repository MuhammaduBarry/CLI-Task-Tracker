from typing import Annotated, Optional
import typer
from rich import print
from rich.console import Console
from rich.table import Table

app = typer.Typer()

tasks = []
@app.command()
def create_task(id_number: Annotated[int, typer.Argument()],
                description: Annotated[Optional[str], typer.Argument()],
                status: Annotated[str, typer.Argument(help='status: todo, in-progress, done')],
                created_at: str,
                updated_at: str):
    """Create a new task"""
    task = {
        'id': id_number,
        'description': description,
        'status': status,
        'createdAt':created_at,
        'updatedAt': updated_at
    }
    tasks.append(task)
    return task


@app.command()
def hello():
    print("hello world")

if __name__ == '__main__':
    app()