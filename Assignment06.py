# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# qinlaura,11/23/2020,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = 'ToDoFile.txt'  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ''  # Captures the user option selection
intIndex = None  # Captures the index of the task to remove from the list
strPriority = ''  # Captures the user priority data
strStatus = ''  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """
        Reads data from a file into a list of dictionary rows
        :param file_name: name of the file (str)
        :param list_of_rows: the list you want filled with file data (list)
        :return: run status (str)
        """
        try:
            list_of_rows.clear()  # clear current data
            file = open(file_name, 'r')
            for line in file:
                task, priority = line.split(',')
                row = {'Task': task.strip(), 'Priority': priority.strip()}
                list_of_rows.append(row)
            file.close()
            run_status = 'Success'
        except:
            run_status = 'Fail'
        return run_status

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """
        Add a task and a priority into the list
        :param task: the new task (str)
        :param priority: the priority of the new task (str)
        :param list_of_rows: the data (list)
        :return: run status (str)
        """
        try:
            list_of_rows.append({'Task': task.strip(), 'Priority': priority.strip()})
            run_status = 'Success'
        except:
            run_status = 'Fail'
        return run_status

    @staticmethod
    def remove_data_from_list(index, list_of_rows):
        """
        Remove an entry from the list by its index
        :param index: the index of the item you'd like to remove (int)
        :param list_of_rows: the data (list)
        :return: run status (str)
        """
        try:
            del list_of_rows[index - 1]
            run_status = 'Success'
        except:
            run_status = 'Fail'
        return run_status

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """
        Write data in list of dictionaries to file, then save and close file
        :param file_name: the name of the file (str)
        :param list_of_rows: the data (list)
        :return: run status (str)
        """
        try:
            file = open(file_name, 'w')
            for item in list_of_rows:
                file.write(item['Task'] + ',' + item['Priority'] + '\n')
            file.close()
            run_status = 'Success'
        except:
            run_status = 'Fail'
        return run_status

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """
        Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Show Current Data
        6) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """
        Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """
        Shows the current Tasks in the list of dictionaries rows
        :param list_of_rows: data you want to display (list)
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def print_current_Tasks_in_list_for_removal(list_of_rows):
        """
        Shows the current Tasks in the list of dictionaries
        rows so that user can select which task to delete
        :param list_of_rows: data you want to display (list)
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for i in range(len(list_of_rows)):
            row = list_of_rows[i]
            print(f"#{i+1} | {row['Task']} ({row['Priority']})")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """
        Gets a yes or no choice from the user
        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """
        Pause program and show a message before continuing
        :param optional_message:  An optional message you want to display (str)
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """
        Prompts user for a new task and priority entry
        :return: a tuple of two strings, task and priority (tuple)
        """
        task = input('Enter a task: ')
        priority = input('Enter the priority of the task: ')
        return task, priority

    @staticmethod
    def input_index_to_remove(list_of_rows):
        """
        Get the index of the task the user wants to delete
        :param list_of_rows: the data, for getting the range of selection (list)
        :return: the index to remove (int)
        """
        list_length = len(list_of_rows)
        index = input(f'Which task would you like to remove? [1-{list_length}]')
        return int(index)

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        strTask, strPriority = IO.input_new_task_and_priority()
        strStatus = Processor.add_data_to_list(strTask, strPriority, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        IO.print_current_Tasks_in_list_for_removal(lstTable)
        intIndex = IO.input_index_to_remove(lstTable)
        strStatus = Processor.remove_data_from_list(intIndex, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            strStatus = Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            strStatus = Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif strChoice == '5': # Print current data
        IO.print_current_Tasks_in_list(lstTable)
        IO.input_press_to_continue()
        continue

    elif strChoice == '6':  #  Exit Program
        print("Goodbye!")
        break   # and Exit

    else:
        print('Sorry, that\'s an invalid option')
        IO.input_press_to_continue()
        continue
