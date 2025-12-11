# Task-Tracker
A CLI app to track your tasks and manage your to-do list.
## Features
- Add, Update, and Delete tasks

- Mark a task as in progress or done

- List all tasks

- List all tasks that are done

- List all tasks that are not done

- List all tasks that are in progress
## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/zokomom/Task-Tracker.git
    ```
2. Navigate to the project directory:
    ```bash
    cd task-tracker
    ```
3. Run the application:
    ```bash
    python task_tracker.py    #in Windows
    pyhton3 task_tracker.py    #in Linux/MacOS
    ```
4. Change Permissions (For Linux/MacOS):
    ```bash
    chmod +x task_tracker.py
    ```
5. Example Commands(For Linux/MacOS): 
    ```bash
        # Adding a new task
        ./task-cli.py add "Buy groceries"
        # Output: Task added successfully (ID: 1)

        # Updating and deleting tasks
        ./task-cli.py update 1 "Buy groceries and cook dinner"
        task-cli.py delete 1

        # Marking a task as in progress or done
        ./task-cli.py mark-in-progress 1
        ./task-cli.py mark-done 1

        # Listing all tasks
        ./task-cli.py list all

        # Listing tasks by status
        ./task-cli.py list done
        ./task-cli.py list todo
        ./task-cli.py list in-progress
    ```
6. Example Commands(For Windows): 
    ```bash
        # Adding a new task
        python task-cli.py add "Buy groceries"
        # Output: Task added successfully (ID: 1)

        # Updating and deleting tasks
        python task-cli.py update 1 "Buy groceries and cook dinner"
        python task-cli.py delete 1

        # Marking a task as in progress or done
        python task-cli.py mark-in-progress 1
        python task-cli.py mark-done 1

        # Listing all tasks
        python task-cli.py list all

        # Listing tasks by status
        python task-cli.py list done
        python task-cli.py list todo
        python task-cli.py list in-progress
    ```
## Usage
Run the application and follow the on-screen prompts to manage your tasks.
## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.
## Acknowledgements
Roadmap.sh - https://roadmap.sh/projects/task-tracker
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

