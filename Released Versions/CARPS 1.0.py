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
def Greeting():
    print("Welcome to the Project Creator!")
    print("This program will ask you for the name of a new .NET project,")
    print("and then generate a text file with the commands to create that project.")
    print("________________________________________________________________________")
    print(" ")

"""
GetProjectName function prompts the user to enter the name of the project and stores it in the global variable ProjectName. It then prints the project name and returns it.

Parameters: None

Returns:
str: The name of the project entered by the user.
"""
def GetProjectName():
    global ProjectName
    ProjectName = input("Enter the name of the project: ")
    print(f"The project name is {ProjectName}.")
    return ProjectName

def CreateCommandText(ProjectName):
    commands = f"""
    mkdir {ProjectName} && \\
    cd {ProjectName} && \\
    dotnet new sln -n {ProjectName} && \\
    dotnet new console -o {ProjectName} && \\
    dotnet sln add {ProjectName}/{ProjectName}.csproj
    """
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

def SuccessfulInstruction:
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