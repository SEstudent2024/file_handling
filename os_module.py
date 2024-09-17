# 1. Exploring Python's OS Module
# Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

# Task 1: Directory Inspector:
# Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.
# List and print all files and subdirectories in the given path
# Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. 
# Handle exceptions for invalid paths or inaccessible directories.
# Code Example:
import os

def list_directory_contents(path):
    try:
        if os.path.isdir(path):
            print(f"Content of directory '{path}': ")
            for enrty in os.listdir(path):
                print(enrty)
        else:
            print(f"Error: The provided path '{path}' is not a valid directory.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{path}'.")
    except FileNotFoundError:
        print(f"Error: The dierctory '{path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)
