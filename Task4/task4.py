import sys

def get_command_line_arguments():
    arguments = sys.argv[1:]  # Exclude the script name itself
    return arguments

# Usage example
arguments = get_command_line_arguments()
print("Command-line arguments:", arguments)
