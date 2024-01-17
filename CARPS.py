# C# Automated Rapid Project Setup (CARPS)

# Python script to create a shell script file
# that will create a new project with a solution file
# Python script to create a text file with the commands to create a new project

import os
def Greeting():
    print("Welcome to the Project Creator!")
    print("This program will ask you for the name of a new .NET project,")
    print("and then generate a text file with the commands to create that project.")
    print("________________________________________________________________________")
    print(" ")

def GetProjectName():
    global ProjectName
    ProjectName = input("Enter the name of the project: ")
    print(f"The project name is {ProjectName}.")

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
    commands = CreateCommandText(project_name)
    CheckTextFile(project_name)

# Call the main function
Main()