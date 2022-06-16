import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from database import *

console = Console()

app = typer.Typer()

@app.command(short_help='adds an item with task name, priority, and category.')
def add(task: str, priority: str, category: str):
    todo = Todo(task, priority, category)
    insert_todo(todo)
    show()

@app.command(short_help='used item ID to delete')
def delete(position: int):
    delete_todo(position-1)
    show()

@app.command(short_help='used item ID to modify')
def update(position: int, task: str, priority: str, category: str):
    update_todo(position-1, task, priority, category)
    show()

@app.command(short_help='used item ID to mark it completed')
def complete(position: int):
    complete_todo(position-1)
    show()

@app.command(short_help='show the entire table')
def show():
    tasks = get_all_todos()
    console.print("[medium_purple3]Todo Lists[/medium_purple3]!", "🖋")

    table = Table(show_header=True, header_style="slate_blue1")
    table.add_column("⏳ ID", style="dim", width=6)
    table.add_column("🎯 Task Name", min_width=25)
    table.add_column("📈 Priority", min_width=8, justify="right")
    table.add_column("〰 Category", min_width=10, justify="right")
    table.add_column("👌 Status", min_width=6, justify="right")
    table.add_column("📅 Date_add", min_width=6, justify="right")
    table.add_column("📆 Date_complete", min_width=6, justify="right")
    

    def get_category_color(category):
        COLORS = {'Work': 'cyan1', 'School': 'chartreuse1', 'Life': 'magenta3', 'Study': 'khaki3'}
        if category in COLORS:
            return COLORS[category]
        return 'white'

    def get_priority_color(prioriy):
        COLORS ={'High': 'bright_red', 'Medium': 'bright_yellow', 'Low': 'bright_green' }
        if prioriy in COLORS:
            return COLORS[prioriy]
        return 'white'
    
    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        c2 = get_priority_color(task.priority)
        task_color = 'sky_blue1'
        is_done_str = '✅' if task.status == 2 else '❎'
        date_complete = task.date_completed if task.status == 2 else None
        table.add_row(str(idx),f'[{task_color}]{task.task}[/{task_color}]', f'[{c2}]{task.priority}[/{c2}]',
                      f'[{c}]{task.category}[/{c}]', is_done_str, task.date_added, date_complete)
    console.print(table)


if __name__ == "__main__":
    app()