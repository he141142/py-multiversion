from multiversion.py3_11 import python_taskb
from multiversion.py3_9 import python_taska
import subprocess
from job_Config import JobConfig, PyEnv
from task import Task
from job import Job, load_job_from_file
def main():
    print("Hello, World!")
    
if __name__ == "__main__":
    # subprocess.run(["D:\python\python.exe", "./multiversion/py3_9/python_taska.py"], check=True)
    
    # py_3_9 = PyEnv("D:\python\python.exe", "3.9")
    # py_3_11 = PyEnv("D:\python\python.exe", "3.11")

    # job_config = JobConfig({"3.9": py_3_9, "3.11": py_3_11})
    
    # job_config.invoke_task_by_version("3.11", "./multiversion/py3_9/python_taska.py")
    
    load_job_from_file("job.json").create_job_config().run_all_tasks()
    main()
    


# import subprocess

# def run_task(python_executable, script_path):
#     try:
#         # Run the specific Python executable with the script
#         subprocess.run([python_executable, script_path], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error running {script_path} with {python_executable}: {e}")
#     except FileNotFoundError as e:
#         print(f"Python executable not found: {python_executable} - {e}")

# if __name__ == "__main__":
#     tasks = [
#         {"python": "/usr/bin/python3.9", "script": "task_a.py"},
#         {"python": "/usr/bin/python3.11", "script": "task_b.py"}
#     ]

#     for task in tasks:
#         run_task(task["python"], task["script"])