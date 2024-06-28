from datetime import date, timedelta, datetime


class Task:
    status_dict = {True: "Done", False: "To do"}
    allowed_priorities = (1, 2, 3)

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

    def mark_as_complete(self):
        if not self.is_complete:
            self.is_complete = True
        else:
            print("Zadanie już zostało ukończone")

    def change_priority(self, new_priority):
        if new_priority in self.allowed_priorities:
            self.priority = new_priority
        else:
            print("Niepoprawna wartość priorytetu")

    def log_time(self, time_logged):
        if isinstance(time_logged, timedelta):
            self.time_logged += time_logged
        else:
            raise TypeError("Podaj wartość w formie timedelta")


    def add_comment(self, comment):
        if self._validate_comment(comment):
            self.comments.append(comment)
        else:
            raise ValueError("Komentarz powinien byc slownikiem o kluczach autor i text")

    @staticmethod
    def _validate_comment(comment):
        if isinstance(comment, dict):
            if "text" in comment and "author" in comment:
                if isinstance(comment["text"], str) and isinstance(comment["author"], str):
                    return True
        return False

