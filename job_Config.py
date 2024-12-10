
import subprocess
from task import Task
from task_decorator import task_decorator
class PyEnv:
    executable_path: str
    version: str
    metadata: dict
    
    def __init__(self,executable_path: str,version: str) -> None:
        self.executable_path = executable_path
        self.version = version
    
    def invoke(self, task_path: str) -> None:
        subprocess.run([self.executable_path,task_path], check=True)
    



class JobConfig:
    
    job_pool: list[callable] = []
    
    py_env: dict[str, PyEnv]
    def __init__(self,py_env: dict[str,PyEnv]) -> None:
        self.py_env = py_env
    
    def get_pyenv(self, version: str) -> PyEnv:
        return self.py_env[version]
    
    def invoke_task_by_version(self, version: str, task_path: str) -> None:
        print(f"Invoking task {task_path} with Python version {version}")
        self.get_pyenv(version).invoke(task_path)
    
    def inject_tasks_to_job_config(self, tasks: list[Task], task_folder:str) -> None:
        for task in tasks:
        # Define the task execution function
            @task_decorator(task)  # Pass the Task object to the decorator
            def run_task(task=task):  # Use default argument to bind the current task
                self.invoke_task_by_version(task.version, f"{task_folder}/{task.task_file}")
            self.job_pool.append(run_task)
            
    def run_all_tasks(self) -> None:
        for task in self.job_pool:
            task()