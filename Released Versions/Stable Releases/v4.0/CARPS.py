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
Version: 4.0

Note: Ensure Python 3.x and .NET SDK are installed before running this script.
"""


import os
import subprocess

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
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            print(f"Failed to execute command: {command}")
            print(f"Error: {stderr.decode()}")
        else:
            print(f"Successfully executed command: {command}")
            print(f"Output: {stdout.decode()}")

# This is the main program that calls the other functions
def main():
    """
    Main program that calls the other functions.
    """
    project_name = input("Enter the name of the project: ")
    execute_commands(project_name)

# Call the main function
main()