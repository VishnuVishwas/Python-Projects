import os

def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write("Hello world!\n")
        print("File" + filename + " created succuessfuly")
    except IOError:
        print("Could not create file " + filename)

def read_file(filename):
    try:
        with open(filename, "r") as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Could not read file " + filename)

def append_file(filename, text):
    try:
        with open(filename, "a") as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Could not append to file " + filename)

def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully" )
    except IOError:
        print("Could not reanme file " + filename)

def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Could not delete file " + filename)

if __name__ == '__main__':
    pass