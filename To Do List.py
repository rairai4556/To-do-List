'''
The Python program acts as a straightforward console-based task management tool. It enables interaction with a to-do list confined in a text document (cps109_a1_output.txt). The application comes with multiple features: 
Task Display: Presents all current tasks within the to-do list document. 
Task Addition: Grants the ability to the users to append a fresh task to the to-do list.
Task Completion: Allows users to label a task as completed by dictating its content to delete. 
Exit: Facilitates termination of the program. 

Functionality Details:

Menu Illustration: The application proposes a menu to users, inciting them to select an operation by typing a corresponding numeral. 

Interaction Management: Users are encouraged to submit their selection or task details. The application confirms the input, making sure it is within the permitted menu boundaries or accepts task details for its addition or completion. 

File Handling: The application performs several file-related actions using Python's file execution methods (open, read, write). It extracts tasks from the document, appends new ones, and expunges completed tasks based on user interaction.

Error Management: The application integrates error management for possible scenarios like file unavailability, input/output obstacles, or erroneous user interactions. 

Content Administration: Tasks are retained as separate lines within the text document. Users can see existing tasks, incorporate new tasks, and designate specific tasks as completed by removing them from the document.

Instructions:
Run the program in a Python environment.
Choose options from the displayed menu by entering the corresponding number:
1: Show existing tasks.
2: Add a new task by entering its content.
3: Mark a task as completed by specifying its content.
4: Exit the program.
Note: Users can interact with the program until they choose to exit (4). Adjustments to the file path (file_path) can be made to use a different file location or name for the to-do list file.

'''
import os
import sys

file_path = "output.txt"

# Function to display the menu and handle user input
def main():
    while True:
        print("Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")
        choice = user_input(True,"x")  # Takes user input within the menu range
        process(choice)  # Processes the user's choice

# Process user choice
def process(choice):
    # choice 1 is show task
    if choice == 1:
        show_task(file_path)
    # choice 2 is add task
    if choice == 2:
        add_task(user_input(False,"add"), file_path)
    # choice 3 is delete file
    if choice == 3:
        complete_task(file_path, user_input(False,"complete"))
    # choice 4 is exit the program
    if choice == 4:
        sys.exit()

# Function to take user input
def user_input(flag,y):
    if flag:
        while True:
            try:
                x = int(input("Enter your choice: "))
                if 0 < x < 5:  # Ensures the input is within the menu range
                    return x
            except:
                pass
    else:
        x = input(f"Enter the task to {y}: ")
        return x

# Function to add a task to the file
def add_task(x, file_path):
    if os.path.exists(file_path):
        mode = 'a'  # If file exists, open in append mode
    else:
        mode = 'w'  # If file doesn't exist, open in write mode
    try:
        with open(file_path, mode) as file:
            file.write(x + '\n')  # Adds the task to the file
        print("Task added successfully.")
    except IOError:
        print("Error adding task to the file.")

# Function to display tasks in the file
def show_task(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()  # Read and display the file content
            print(content)
    except FileNotFoundError:
        print("File not found.")

# Function to mark a task as completed by deleting it from the file
def complete_task(file_path, content_to_delete):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  # Read all lines from the file
        with open(file_path, 'w') as file:
            line_deleted = False
            for line in lines:
                if content_to_delete not in line:
                    file.write(line)  # Rewrite lines except the one to be deleted
                else:
                    line_deleted = True
            if line_deleted:
                print(f"'{content_to_delete}' is completed")
            else:
                print(f"'{content_to_delete}' not found in the file.")
                # error if the file is not found 
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error deleting the line from the file.")

if __name__ == "__main__":
    main()
