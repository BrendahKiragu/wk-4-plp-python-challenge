# This program:
#   1. Prompts the user for the name of the input file.
#   2. Prompts the user for the name of the output file.
#   3. Reads the content of the input file.
#   4. Converts the text to uppercase.
#   5. Writes the modified content into the new file.
#   6. Handles file-related errors gracefully.

def read_and_write_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        
        modified_content = content.upper()
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content written to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except IOError:
        print(f"Error: The file {input_file} could not be read.")

# Example usage
read_and_write_file(input("Enter file name: "), input("Enter the name of the new file: "))


# How to run: python3 script.py