# CARPS
# **C# Automated Rapid Project Setup (CARPS) Documentation**

## **Introduction**

CARPS (C# Automated Rapid Project Setup) is a Python-based automation tool designed to streamline the setup of new C# projects. It automates the creation of a new .NET project, including the generation of a solution file and project directory structure.

## **Installation**

### **Prerequisites**

- Python 3.x installed on your machine.
- .NET SDK installed for C# project development.

### **Setup**

1. Clone or download the CARPS repository from its source.
2. Navigate to the downloaded folder.
3. Ensure Python is properly installed by running **`python --version`** in your terminal.

## **Usage**

### **Starting the Script**

- Run the script using the command: **`python carps.py`**.
- Follow the on-screen prompts to enter the project name.

### **Generated Output**

- The script will create a text file containing the commands needed to set up the new C# project.

## **Features**

1. **Interactive Menu System**: Allows users to select actions like creating new projects or adding projects to an existing solution.
2. **Logging System**: Records activities and errors encountered during the execution of the script.
3. **Project Templates**: Offers various templates for different types of C# projects.
4. **Configurable Settings**: Users can set default behaviors through a configuration file.
5. **Version Control Integration**: Initializes a Git repository and commits the initial project structure.

## **Troubleshooting**

- **Script not starting**: Ensure Python is correctly installed and the script file **`carps.py`** is in the current directory.
- **.NET SDK errors**: Confirm that the .NET SDK is installed and properly configured on your machine.
- **File permission issues**: Make sure you have the necessary permissions to create files and directories in the chosen location.

## **Contact**
