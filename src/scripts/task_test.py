from datetime import date, datetime, timedelta
from classes.task import Task

data_base = {
            "description": "Learn Python",
            "assignee": "Andrzej",
            "due_date": "2023-11-12",
            "priority": 3,
            "time_logged": 0.0,
            "is_complete": False,
            "tags": [
                "coding",
                "python"
            ],
            "comments": []
        }

new_task = Task(data_base)
print(new_task.is_complete)

new_task.mark_as_complete()
print(new_task.is_complete)

new_task.mark_as_complete()

# ----
print(new_task.priority)
new_task.change_priority(24)
print(new_task.priority)

# ----
print(new_task.time_logged)
new_task.log_time(timedelta(seconds=34))
print(new_task.time_logged)
