
import json

class Task:
    def __init__(self, version: str, task_file: str,executable_path: str):
        self.version = version
        self.task_file = task_file
        self.executable_path = executable_path

    def __repr__(self):
        return f"Task(version={self.version}, task_file={self.task_file}, executable_path={self.executable_path})"
    


