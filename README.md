# C# Automated Rapid Project Setup (CARPS)

## Overview

CARPS is a Python script that automates the setup of new C# projects. It streamlines the project initialization process by generating a series of commands to create a .NET project and solution file.

## Features

* Interactive prompts for project name input.
* Validation of project name.
* Creation of a new directory for the project.
* Initialization of a new .NET solution.
* Creation of a new console application.
* Addition of the application to the solution.
* Building and running the application.
* Error handling for command execution.

## Functions

### greeting()

Prints a welcome message to the user.

### get_project_name()

Prompts the user to input the name of the project and returns the input as a string.

### validate_project_name(project_name)

Validates the project name. The project name must be non-empty and can only contain alphanumeric characters and underscores. If the project name is invalid, it raises a ValueError.

### execute_single_command(single_command)

Executes a single command using the subprocess module. It prints the command being executed and the output of the command. If the command fails, it prints an error message and stops the execution of the program.

### execute_dotnet_commands(project_name)

Creates the necessary directories for the project and constructs a list of .NET commands to be executed. It then calls `execute_single_command` for each command in the list.

### main()

The main function of the program. It parses command line arguments, gets the project name if not provided, validates the project name, and executes the necessary commands to set up the .NET project.

## Usage

Run this script in a Python environment. Follow the prompts to input the name of the new project. The script will generate a series of commands to set up the project.

## Requirements

* Python 3.x
* .NET SDK

## Created by

John Akujobi

## Date

January 2024

## Version

5.0
