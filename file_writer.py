'''
filename: file_writer.py

This program will ask the user for sentences to write to a file.
If the user has no more sentences to add, the program terminates.

1. Ask the user for the filename. If no parameters given, filename will default to mylife.txt
    - If a file already exists, open that file.
    - If the file is new, create a new one.
2. Ask the user for input, and then append that input to the file.

'''

# Ask the user for the filename. If no parameters given, filename will default to mylife.txt
def file_writer(text, filename):
    filename = 'mylife.txt' if filename == '' else filename
    with open(filename, 'a') as file_to_write:
        # Ask the user for input, and then append that input to the file.
        file_to_write.write(f'{text}\n')