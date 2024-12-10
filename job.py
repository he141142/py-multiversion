from task import Task
from job_Config import JobConfig, PyEnv
import json

class Job:
    def __init__(self, name: str, task_folder: str, tasks: list[Task]):
        self.name = name
        self.task_folder = task_folder
        self.tasks = tasks

    def __repr__(self):
        return f"Job(name={self.name}, task_folder={self.task_folder}, tasks={self.tasks})"
    
    def create_job_config(self)->JobConfig:
        py_env: dict[str,PyEnv] = {}
        for task in self.tasks:
            py_env[task.version] = PyEnv(task.executable_path,task.version)
        job_config =  JobConfig(py_env)
        job_config.inject_tasks_to_job_config(self.tasks,self.task_folder)
        return job_config
    
    
def load_job_from_file(file_path: str) -> Job:
    with open(file_path, 'r') as f:
        data = json.load(f)

    tasks = [Task(task['version'], task['task_file'], task['executable_path']) for task in data['tasks']]
    return Job(data['name'], data['task_folder'], tasks)