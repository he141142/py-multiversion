from functools import wraps
import time
from task import Task
import subprocess

# Parameterized decorator
def task_decorator(task: Task):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Starting task: {task.task_file} (Python {task.version})")
            print(f"Using executable: {task.executable_path}")
            start_time = time.time()
            
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                print(f"Task {task.task_file} failed with error: {e}")
                return None
            finally:
                end_time = time.time()
                print(f"Task {task.task_file} completed in {end_time - start_time:.2f} seconds")
            
            return result
        return wrapper
    return decorator