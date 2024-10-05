TASKS_FILE = 'tasks.txt'


def add_task(task_name):
    """Thêm công việc vào file tasks.txt."""
    with open(TASKS_FILE, 'a') as file:  # Chế độ ghi "a" để thêm vào
        # Tạo ID cho công việc mới
        tasks = read_tasks()
        task_id = len(tasks) + 1  # Tạo ID mới dựa trên số công việc hiện có
        file.write(f"{task_id}, {task_name}, False\n")  # Ghi công việc vào file với trạng thái chưa hoàn thành


def displays_tasks():
    """Hiển thị danh sách các công việc."""
    tasks = read_tasks()
    if len(tasks) == 0:
        print('Not found task!')
    else:
        for task in tasks:
            status = 'completed' if task['completed'] else 'not completed'
            print("{}: {} ({})".format(task['id'], task['name'], status))


def read_tasks():
    """Đọc danh sách các công việc từ file."""
    tasks = []
    try:
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                # Mô tả định dạng trong file
                parts = line.strip().split(', ')
                task_id = int(parts[0])
                task_name = parts[1]
                completed = (parts[2] == 'True')
                # Thêm dữ liệu vào tasks
                tasks.append({"id": task_id, "name": task_name, "completed": completed})
    except FileNotFoundError:
        print(f"File {TASKS_FILE} not found.")
    return tasks  # Trả về danh sách công việc


def remove_task(task_id):
    """Xóa công việc theo ID."""
    try:
        tasks = read_tasks()
        new_tasks = []
        for task in tasks:
            if task['id'] != task_id:
                new_tasks.append(task)    
        with open(TASKS_FILE, 'w') as file:
            for task in new_tasks:
                file.write(f"{task['id']}, {task['name']}, {task['completed']}\n")
        print(f"Delete task with ID = {task_id} success.")
    except FileNotFoundError:
        print(f"File {TASKS_FILE} not found!.")

def update_task(task_id):
    tasks = read_tasks()
    for task in tasks:
        if task['id'] == task_id:
            print("Current task: {} - {}".format(task['name'], task['completed'] == True))
            print("Do you want to update    task name? (y/n)")
            choice = input()
            if choice == 'y':
                task['name'] = input('New task name: ')
            elif choice == 'n':
                """Do nothing"""
            else:
                print("Invalid choice")
            print("Do you want to update task status? (y/n)")
            choice = input()
            if choice == 'y':
                print("Current status: {}".format(task['completed'] == True))
                task['completed'] = not task['completed']
                print("Task status updated to: {}".format(task['completed'] == True))
            elif choice == 'n':
               """Do nothing"""
            else:
                print("Invalid choice")
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task['id']}, {task['name']}, {task['completed']}\n")
    print("Task updated.")
    
def search_task_by_id(task_id):
    tasks = read_tasks()
    found_tasks = {}
    for task in tasks:
        if task['id'] == task_id:
            found_tasks = task   
    if len(found_tasks) == 0:
        print("Task not found.")
    else:
        print("Found task: {} - {}".format(found_tasks['name'], found_tasks['completed'] == True))
def main():
    while True:
        print("\nMenu")
        print('1. Add task')
        print('2. Delete task')
        print('3. View all task')
        print('4. Update task')
        print('5. Find task by id')
        print('6. Exit')

        choice = int(input('Enter choice: '))

        if choice == 1:
            task_name = input('Input task name: ')
            add_task(task_name)
        elif choice == 2:
            task_id = int(input('Input task ID to delete: '))
            remove_task(task_id)
        elif choice == 3:
            displays_tasks()
        elif choice == 4:
            task_id = int(input('Input task ID to update: '))
            update_task(task_id)
        elif choice == 5:
            task_id = int(input('Input task ID to search: '))
            search_task_by_id(task_id)
        elif choice == 6:
            print("Exit.")
            break
        else:
            print('Input again!')        

if __name__ == "__main__":
    main()
