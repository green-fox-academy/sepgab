# write a function that takes a filename and returns the number of lines the
# file contains. It should return zero if the file does not exist.

def line_counter(file_name):
    try:
        my_file = open(file_name, "r")
        lines = my_file.readlines()
        print(len(lines))
    except FileNotFoundError:
        print(0)

line_counter("reversed.txt")
line_counter("reversed-lines.txt")
