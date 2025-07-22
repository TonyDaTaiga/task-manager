from src.task_manager import TaskManager
import sys
from colorama import init, Fore, Style

#colorama gives window color support

init()

def print_usage():
    print(f"""
    {Fore.CYAN}Task Manager Commands:{Style.RESET_ALL}
    python main.py add "Title" "Description" "Due Date" "Priority"end=
    python main.py list
    python main.py complete "Title"
    python main.py delete "Title"
    
    {Fore.Yellow}Priority can be: LOW, MEDIUM, or HIGH{Style.RESET_ALL}
    """)

def main():
    manager = TaskManager()

    if len(sys.argv) < 2:
        print_usage()
        return
    
    command = sys.argv[1].lower()

    try:
        if command == "add":

            if len(sys.argv) != 6:

                print(f"{Fore.RED}Error: Add command requires title, description, due date, and priority{Style.RESET_ALL}")

                return

            title = sys.argv[2]

            description = sys.argv[3]

            due_date = sys.argv[4]

            priority = sys.argv[5]

            if manager.add_task(title, description, due_date, priority):

                print(f"{Fore.GREEN}Task '{title}' added successfully!{Style.RESET_ALL}")


        elif command == "list":

            tasks = manager.list_tasks()

            if not tasks:

                print(f"{Fore.YELLOW}No tasks found.{Style.RESET_ALL}")

            for task in tasks:

                status = "✓" if task.completed else " "

                color = Fore.GREEN if task.completed else Fore.WHITE

                print(f"{color}[{status}] {task.title} - Due: {task.due_date} (Priority: {task.priority}){Style.RESET_ALL}")


        elif command == "complete":

            if len(sys.argv) != 3:

                print(f"{Fore.RED}Error: Complete command requires a task title{Style.RESET_ALL}")

                return

            title = sys.argv[2]

            if manager.complete_task(title):

                print(f"{Fore.GREEN}Task '{title}' marked as complete!{Style.RESET_ALL}")

            else:

                print(f"{Fore.RED}Task '{title}' not found!{Style.RESET_ALL}")


        elif command == "delete":

            if len(sys.argv) != 3:

                print(f"{Fore.RED}Error: Delete command requires a task title{Style.RESET_ALL}")

                return

            title = sys.argv[2]

            if manager.delete_task(title):

                print(f"{Fore.GREEN}Task '{title}' deleted!{Style.RESET_ALL}")

            else:

                print(f"{Fore.RED}Task '{title}' not found!{Style.RESET_ALL}")


        else:

            print_usage()


    except Exception as e:

        print(f"{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}")


if __name__ == "__main__":

    main()