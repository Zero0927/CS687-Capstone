
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

class Todo:
    def __init__(self, task, priority, category, 
                 date_added=None, date_completed=None,
                 status=None, position=None):
        self.task = task
        self.category = category
        self.priority= priority
        self.date_added = date_added if date_added is not None else dt_string
        self.date_completed = date_completed if date_completed is not None else dt_string
        self.status = status if status is not None else 1  # 1 = open, 2 = completed
        self.position = position if position is not None else None

    def __repr__(self) -> str:
        return f"({self.task}, {self.category},{self.priority}, {self.date_added}, {self.date_completed}, {self.status}, {self.position})"