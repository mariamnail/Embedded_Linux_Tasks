import sys

def get_arguments():
    arguments = sys.argv[:]  
    return arguments

arguments = get_arguments()
print("Command-line arguments:", arguments)
