from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority 
        self.completed = False
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date":str(self.due_date),
            "priority": self.priority,
            "completed": self.completed,
            "created_at": str(self.created_at)        
        }