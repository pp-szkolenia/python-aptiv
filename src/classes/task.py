from datetime import date, timedelta


class Task:
    def __init__(self, task_data: dict):
        self.description = task_data["description"]
        self.assignee = task_data["assignee"]
        self.due_date = task_data["due_date"]
        self.piority = task_data["piority"]
        self.time_logged = task_data["time_logged"]
        self.is_complete = task_data["is_complete"]
        self.tags = task_data["tags"]
        self.comments = task_data["comments"]
