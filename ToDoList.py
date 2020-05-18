# ------------------------------------------------------------------------ #
# Title: Assignment05 (To Do List)
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a Python Dictionary.
#              Add each dictionary "row" to a Python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.20,Created script
# MGidd,5.14.20,Added code for processing
# MGidd,5.15.20,Added code for input/output
# MGidd,5.16.20,Cleaned up code,added formatting for visual output
# ------------------------------------------------------------------------ #

# -- Data -- #
# Declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""    # A row of text data from the file
dicRow = {}     # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []   # A list that acts as a 'table' of rows
strMenu = ""    # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a Python list of dictionary rows
loadFile = open(objFile, "r")
for row in loadFile:
    lstRow = row.split(",")
    dicRow = {"task": lstRow[0], "priority": lstRow[1].strip()}
    lstTable.append(dicRow)
loadFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current tasks
    2) Add a new task
    3) Remove an existing task
    4) Save tasks to file
    5) Exit program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task" + ' | ' + "Priority")
        for row in lstTable:
            print(row["task"] + ": " + row["priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print('Enter a task and the level of priority.')
        strTask = input('Task: ')
        strPriority = input('Priority: ')
        dicRow = {"task": strTask, "priority": strPriority}
        lstTable.append(dicRow)
        print("Task added!")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemove = input("Task to remove: ")
        for row in lstTable:
            if row["task"].lower() == strRemove.lower():
                lstTable.remove(row)
                print("Task removed!")
                break
        if dicRow["task"].lower() != strRemove.lower():
            print("Task not found!")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        loadFile = open("ToDoList.txt", 'w')
        for row in lstTable:
            loadFile.write(str(row["task"]) + ',' + str(row["priority"]) + '\n')
        loadFile.close()
        print("Tasks saved to file!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        strExit = input("Do you want to save your tasks before exiting? Enter 'y' or 'n': ")
        if strExit == "y":
            loadFile = open("ToDoList.txt", 'w')
            for row in lstTable:
                loadFile.write(str(row["task"]) + ',' + str(row["priority"]) + '\n')
            loadFile.close()
            print("\n" + "Tasks saved. Goodbye!" + "\n")
        elif strExit == "n":
            break
        break  # and Exit the programpy