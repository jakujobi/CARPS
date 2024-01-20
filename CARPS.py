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
Version: 5.0

Note: Ensure Python 3.x and .NET SDK are installed before running this script.
"""


import os
import subprocess
import re

greeting_text = """
C# Automated Rapid Project Setup (CARPS)
Welcome to CARPS!
This application helps you set up a new .NET project.
It will:
- Create a new directory for your project,
- Initialize a new solution,
- Create a new console application,
- Add the application to the solution,
- Build the application, and run it.
Please ensure that .NET SDK are installed.
Let's get started!\n
"""

def greeting():
    print(greeting_text)

def get_project_name():
    project_name = input("Enter the name of the project: ")
    validate_project_name(project_name)
    return project_name

def validate_project_name(project_name):
    if not project_name or not re.match("^[A-Za-z0-9_]+$", project_name):
        raise ValueError("Invalid project name. Project name must be non-empty and can only contain alphanumeric characters and underscores.")

def execute_commands(project_name):
    base_path = os.getcwd()
    project_path = os.path.join(base_path, project_name, project_name)

    commands = [
        f'mkdir "{project_name}"',
        f'mkdir "{project_path}"',
        f'dotnet new sln -n {project_name} -o "{project_path}"',
        f'dotnet new console -o "{os.path.join(project_path, project_name)}"',
        f'dotnet sln "{os.path.join(project_path, f"{project_name}.sln")}" add "{os.path.join(project_path, project_name, f"{project_name}.csproj")}"',
        f'dotnet build "{os.path.join(project_path, project_name, f"{project_name}.csproj")}"',
        f'dotnet run --project "{os.path.join(project_path, project_name, f"{project_name}.csproj")}"'
    ]

    for command in commands:
        print(f"Executing command: {command}")
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            print(f"Failed to execute command: {command}")
            print(f"Error: {stderr.decode()}")
            raise SystemExit("Stopping execution due to command failure.")
        else:
            print(f"Successfully executed command: {command}")
            print(f"Output: {stdout.decode()}")

# This is the main program that calls the other functions
def main():
    """
    Main program that calls the other functions.
    """
    project_name = get_project_name()
    execute_commands(project_name)

if __name__ == "__main__":
    greeting()
    main()