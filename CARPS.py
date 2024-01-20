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
Version: 6.0

Note: Ensure Python 3.x and .NET SDK are installed before running this script.
"""


import os
import subprocess
import re
import argparse
import tkinter as tk
import time
import threading
from tkinter import messagebox

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
    return project_name

def validate_project_name(project_name):
    if not project_name or not re.match("^[A-Za-z0-9_ ]+$", project_name):
        raise ValueError("Invalid project name. Project name must be non-empty and can only contain alphanumeric characters, underscores, and spaces.")

def execute_single_command(single_command):
    print(f"Executing command: {single_command}")
    process = subprocess.Popen(single_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Failed to execute command: {single_command}")
        print(f"Error: {stderr.decode()}")
        print(f"Output: {stdout.decode()}")
        raise SystemExit("Stopping execution due to command failure.")
    else:
        print(f"Successfully executed command: {single_command}")
        print(f"Output: {stdout.decode()}")

def console_execute_dotnet_commands(project_name):
    current_directory = os.getcwd()
    project_directory_path = os.path.join(current_directory, project_name)

    os.makedirs(project_name, exist_ok=True)
    os.makedirs(project_directory_path, exist_ok=True)

    dotnet_commands = [
        f'dotnet new sln -n {project_name} -o "{project_directory_path}"',
        f'dotnet new console -o "{os.path.join(project_directory_path, project_name)}"',
        f'dotnet sln "{os.path.join(project_directory_path, f"{project_name}.sln")}" add "{os.path.join(project_directory_path, project_name, f"{project_name}.csproj")}"',
        f'dotnet build "{os.path.join(project_directory_path, project_name, f"{project_name}.csproj")}"',
        f'dotnet run --project "{os.path.join(project_directory_path, project_name, f"{project_name}.csproj")}"'
    ]

    for single_command in dotnet_commands:
        execute_single_command(single_command)

def execute_dotnet_commands(project_name, loading_label, run_button, status_bar):
    current_directory = os.getcwd()
    project_directory_path = os.path.join(current_directory, project_name)

    os.makedirs(project_name, exist_ok=True)
    os.makedirs(project_directory_path, exist_ok=True)

    dotnet_commands = [
        f'dotnet new sln -n {project_name} -o "{project_directory_path}"',
        f'dotnet new console -o "{os.path.join(project_directory_path, project_name)}"',
        f'dotnet sln "{os.path.join(project_directory_path, f"{project_name}.sln")}" add "{os.path.join(project_directory_path, project_name, f"{project_name}.csproj")}"',
        f'dotnet build "{os.path.join(project_directory_path, project_name, f"{project_name}.csproj")}"',
        f'dotnet run --project "{os.path.join(project_directory_path, project_name, f"{project_name}.csproj")}"'
    ]

    for single_command in dotnet_commands:
        execute_single_command(single_command)

    time.sleep(5)  # Simulate a long-running operation
    stop_loading_animation(loading_label)
    run_button.pack(padx=10, pady=10)  # Show the button again
    status_bar.config(text="Done! Check the directory for your project")
    root.destroy()  # Close the Tkinter window

################################################################



def animate_loading_label(loading_label):
    dots = loading_label.cget("text").count('.')
    if dots < 3:
        loading_label.config(text=loading_label.cget("text") + '.')
    else:
        loading_label.config(text="Loading")

def start_loading_animation(loading_label):
    loading_label.place(x=250, y=100)  # Start the loading animation
    animate_loading_label(loading_label)
    loading_label.after(500, start_loading_animation, loading_label)  # Update every 500 ms

def stop_loading_animation(loading_label):
    loading_label.place_forget()  # Stop the loading animation

def run_program(project_name_entry, loading_label, status_bar, run_button):
    project_name = project_name_entry.get()
    try:
        validate_project_name(project_name)
        status_bar.config(text="Running...")
        run_button.pack_forget()  # Hide the button
        start_loading_animation(loading_label)
        threading.Thread(target=execute_dotnet_commands, args=(project_name, loading_label, run_button, status_bar)).start()
    except Exception as e:
        messagebox.showerror("Error", str(e))



def main():
    parser = argparse.ArgumentParser(description="Set up a new .NET project.")
    parser.add_argument("project_name", nargs='?', default=None, help="The name of the project to create.")
    args = parser.parse_args()

    if args.project_name is not None:
        # Command-line version
        greeting()
        validate_project_name(args.project_name)
        console_execute_dotnet_commands(args.project_name)
    else:
        root = tk.Tk()
        root.title("CARPS - C# Automated Rapid Project Setup")
        root.geometry("500x200")

        loading_label = tk.Label(root, text="Loading", font=("Arial", 14))

        project_name_label = tk.Label(root, text="Project Name:", font=("Arial", 14))
        project_name_label.pack(padx=10, pady=10)  # Add padding

        project_name_entry = tk.Entry(root, font=("Arial", 14))
        project_name_entry.insert(0, "Enter project name here")  # Add default text
        project_name_entry.pack(padx=10, pady=10)

        run_button = tk.Button(root, text="Run Program", command=lambda: run_program(project_name_entry, loading_label, status_bar, run_button), font=("Arial", 14), bg="blue", fg="white", relief=tk.GROOVE, bd=5, highlightbackground="red", highlightcolor="green", activebackground="purple", activeforeground="yellow")
        run_button.pack(padx=10, pady=10)

        clear_button = tk.Button(root, text="Clear", command=lambda: project_name_entry.delete(0, 'end'), font=("Arial", 14))  # Add clear button
        clear_button.pack(padx=10, pady=10)

        status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)  # Add status bar
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        root.mainloop()

if __name__ == "__main__":
    main()