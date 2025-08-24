# This program:
#   1. Prompts the user to input the name of the file they want to read.
#   2. Tries to open the specified file in read mode.
#   3. If successful, reads and prints the file's contents to the console.
#   4. If the file does not exist, displays a clear error message.
#   5. If there is any issue reading the file, handles it gracefully.

def get_filename_and_read():
    filename = input("Please enter the filename: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: The file {filename} cannot be read.")

# Example usage
get_filename_and_read()

# How to run: python3 error.py