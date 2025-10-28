tasks = {
    "write report": "in progress",
    "prepare presentation": "pending",
    "send email to client": "completed",
    "create backup": "pending"
}
def add_task(task_name, status="pending"):
    if task_name in tasks:
        print(f"task {task_name} already exists")
    else:
        tasks[task_name] = status
        print(f"task {task_name} added with status: {status}")
def remove_task(task_name):
    if task_name in tasks:
        del tasks[task_name]
        print(f"task {task_name} removed")
    else:
        print(f"task {task_name} not found")
def change_status(task_name, new_status):
    if task_name in tasks:
        tasks[task_name] = new_status
        print(f"task {task_name} changed to {new_status}")
    else:
        print(f"task {task_name} not found")
def get_pending_tasks():
    return [task for task, status in tasks.items() if status == "pending"]
print("list of tasks:")
for name, status in tasks.items():
    print(f"{name}, status: {status}")
print("adding new task:")
add_task("check report")
print("changing status of task:")
change_status("prepare presentation", "in progress")
print("removing task")
remove_task("send email to client")
print("tasks that are pending:")
pending = get_pending_tasks()
print(pending)