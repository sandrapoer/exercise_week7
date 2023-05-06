import os
names = ['Sarah', 'Lisa', 'Mark', 'Tobias', 'Kerstin', 'Frank', 'Norbert', 'Hannah', 'Isaak', 'Julia']


# QUESTION NR 1
def create_file(filename):
    with open(filename, 'w') as file:
        file.write(','.join(names))


# QUESTION NR 2
def transform_to_row(input_file, output_file):
    # Open file in read mode
    with open(input_file, 'r') as file:
        data = file.read()
    # Split content into words
    words = data.split(',')
    # open output file with write mode and put each word in a new line
    with open(output_file, 'w') as file:
        for word in words:
            file.write(word.strip() + '\n')


# QUESTION NR 3
def add_greeting(input_file, output_file):
    # open and read input file
    with open(input_file, 'r') as input:
        # read content of file and split into lines
        lines = input.readlines()
        words = [word.strip() for line in input for word in line.split(',')]

    # open the output file in write mode
    with open(output_file, 'w') as output:
        # write the new lines to in the output
        output.writw("\n".join(words))
        # add "Hello" in the front of each line
        for word in words:
            output.write(f"Hello {word}\n")


# QUESTION NR 4
def strip_greeting(input_file, output_file):
    # open input in read mode
    with open(input_file, 'r') as input:
        lines = input.readlines()
    # Remove "Hello" and white space " " from each line
    stripped_lines = [line.replace("Hello ", "") for line in lines]
    # open output in write mode
    with open(output_file, 'w') as output:
        for line in stripped_lines:
            # add new text to output file
            output.write(line)


# QUESTION NR 5
def combine_files(file1, file2, output_file):
    # Open file 1 with read mode
    with open(file1, 'r') as f1:
        lines1 = f1.readlines()
    # Open file 2 with read mode
    with open(file2, 'r') as f2:
        lines2 = f2.readlines()

    # Check if both files have the same number of lines
    if len(lines1) != len(lines2):
        return print("Error: Files have different number of lines")

    # Open the output file with write mode
    with open(output_file, 'w') as output:
        # Combine the lines from file 1 and file 2 and add them to the output file
        for line in range(len(lines1)):
            output.write(lines1[line].strip() + ' ' + lines2[line].strip() + '\n')

    print("Combined files written to", output_file)

