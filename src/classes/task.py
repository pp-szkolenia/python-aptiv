from datetime import date, timedelta, datetime


class Task:
    status_dict = {True: "Done", False: "To do"}

    def __init__(self, task_data: dict):
        self.description: str = task_data["description"]
        self.assignee: str = task_data["assignee"]
        self.due_date: date = datetime.strptime(task_data["due_date"], "%Y-%m-%d").date()
        self.priority: int = task_data["priority"]
        self.time_logged: timedelta = timedelta(seconds=task_data["time_logged"])
        self.is_complete: bool = task_data["is_complete"]
        self.tags: list[str] = task_data["tags"]
        self.comments: list[dict[str, str]] = task_data["comments"]

    def __str__(self):
        return "\n".join([f"Description: {self.description}",
                          f"Status: {self.status_dict[self.is_complete]}",
                          f"Assignee: {self.assignee}",
                          f"Due date: {self.due_date}"])

    def jsonify(self):
        result_dict = {'description': self.description,
                       'assignee': self.assignee,
                       'due_date': str(self.due_date),
                       'priority': self.priority,
                       'time_logged': self.time_logged.seconds,
                       'is_complete': self.is_complete,
                       'tags': self.tags,
                       'comments': self.comments}
        return result_dict

    def edit_description(self, new_description):
        if isinstance(new_description, str):
            self.description = new_description
        else:
            print('Podany opis nie jest stringiem')


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
print(new_task)
print(new_task.jsonify())
new_description = 'practice python'
new_task.edit_description(new_description)
print(new_task.description)
