"""
C# Automated Rapid Project Setup (CARPS)

This Python script automates the setup of new C# projects. It generates a text file with 
commands to create a .NET project and solution file, streamlining the project initialization process.

Usage:
Run this script in a Python environment. Follow the prompts to input the name of the new project.
The script will generate a text file with commands to set up the project.

Features:
- Creates a new .NET project and solution file.
- Interactive prompts for project name input.
- Generates a text file with necessary commands for project setup.

Created by: John Akujobi
Date: January 2024
Version: 1.0

Note: Ensure Python 3.x and .NET SDK are installed before running this script.
"""


import os
import platform


def Greeting():
    print("Welcome to the Project Creator!")
    print("This program will ask you for the name of a new .NET project,")
    print("and then generate a text file with the commands to create that project.")
    print("_______________________________________________________________________")
    print(" ")

def get_os():
    operating_system = platform.system()
    if operating_system == "Windows":
        operating_system, terminal = get_user_environment()
        separator = " && " if terminal == "PowerShell" else " & "
    elif operating_system == "Linux":
        operating_system, terminal = "Linux", "Bash"
        separator = " && "
    elif operating_system == "Darwin":
        operating_system, terminal = "Mac", "Bash"
        separator = " && "
    else:
        print("Unknown operating system. \nPlease enter the command separator for your platform (e.g., ' & ' for Command Prompt, ' && ' for PowerShell, Linux, Git Bash, Mac): ")
        separator = input()
        operating_system, terminal = "Unknown", "Unknown"
    return operating_system, terminal, separator

def get_user_environment():
    print("Please select your terminal:")
    print("1. Command Prompt")
    print("2. PowerShell")
    print("3. Other (e.g. Git Bash)")
    terminal_choice = int(input("Enter the number of your choice: "))
    if terminal_choice == 1:
        terminal = "Command Prompt"
    elif terminal_choice == 2:
        terminal = "PowerShell"
    elif terminal_choice == 3:
        print("Other terminal selected.")
        terminal = "PowerShell"
    else:
        print("Invalid choice. Defaulting to Command Prompt.")
        terminal = "Command Prompt"
    return "Windows", terminal

def GetProjectName():
    global ProjectName
    ProjectName = input("Enter the name of the project: ")
    print(f"The project name is {ProjectName}.")
    return ProjectName

def CreateCommandText(project_name):
    operating_system, terminal, separator = get_os()
    commands = f"mkdir {project_name}{separator}\n" \
                f"cd {project_name}{separator}\n" \
                f"dotnet new sln -n {project_name}{separator}\n" \
                f"dotnet new console -o {project_name}{separator}\n" \
                f"dotnet sln add {project_name}/{project_name}.csproj"
    return commands

# Create the text file
def CreateTextFile(commands, project_name):
    # Open the text file in write mode
    # Write the commands to the file
    # Close the file
    # Print a message indicating that the file was created successfully.
    with open(f'{project_name} - Copy into Terminal to create.txt', 'w') as file:
        file.write(commands)
    print ("Creating text file...")

# Check if the text file was created successfully
# Then print a message indicating that the text file was created successfully.
def CheckTextFile(project_name):
    if os.path.exists(f'{project_name} - Copy into Terminal to create.txt'):
        SuccessfulInstruction()
    else:
        FailedInstruction()

def SuccessfulInstruction():
    print("Text file created successfully.")
    print(" ")

def FailedInstruction():
    print("Failed to create text file.")
    print("Please try again.")
    print(" ")
    print("________________________________________________________________________")
    print(" ")

# This is the main program that calls the other functions
def Main():
    Greeting()
    project_name = GetProjectName()
    commands = CreateCommandText(ProjectName)
    CreateTextFile(commands, ProjectName)
    CheckTextFile(ProjectName)

# Call the main function
Main()