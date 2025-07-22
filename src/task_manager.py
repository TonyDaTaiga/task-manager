import json
import os
from pathlib import Path
from .task import Task

class TaskManager:
    def __init__(self):
        #windows style path
        self.filename = Path("data/tasks.json").absolute()
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if self.filename.exists():
            with open(self.filename, "r") as f:
                try:
                    data = json.load(f)
                    for task_data in data:
                        task = Task(
                            task_data["title"],
                            task_data['description'],
                            task_data["due_date"],
                            task_data["priority"]
                        )
                        task.completed = task_data["completed"]
                        self.tasks.append(task)
                except json.JSONDecodeError:
                    print("Error reading tasks file. Starting with empty task list.")
    
    def save_tasks(self):
        #creates directory if none
        self.filename.parent.mkdir(exist_ok=True)

        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2)

    def add_task(self, title, description, due_date, priority):
        try:
            if not title or not description:
                raise ValueError("Title and description cannot be empty")
            
            if priority.upper() not in ["LOW", "MEDIUM", "HIGH"]:
                raise ValueError("Priority must be LOW, MEDIUM, or HIGH")
            
            task = Task(title, description, due_date, priority.upper())
            self.tasks.append(task)
            self.save_tasks()
            return task
        except Exception as e:
            print(f"Error adding task: {str(e)}")
            return None
    
    def list_tasks(self):
        return self.tasks
    
    def complete_task(self,title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.completed = True
                self.save_tasks()
                return True
        return False
        
    def delete_task(self, title):
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.title.lower() != title.lower()]
        if len(self.tasks) < initial_length:
            self.save_tasks()
            return True
        return False