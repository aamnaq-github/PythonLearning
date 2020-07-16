import os

# Problem 92: Implement a program dirtree.py that takes a directory as argument and prints all the files in that
# directory recursively as a tree. Hint: Use os.listdir and os.path.isdir funtions.
def dirtree(dir, level = 1):
    all_files = os.listdir(dir)
    if level > 1:
        if level - 2 == 0:
            print('|-- ', os.path.basename(dir))
        else:
            print('|  ' * (level - 2), '|-- ', os.path.basename(dir))
    for file in all_files:
        if not os.path.isfile(dir + '/' + file):
            dirtree(dir + '\\' + file, level + 1)
        else:
            if all_files[-1] == file:
                print('|   ' * (level - 1), '`-- ', file)
            else:
                print('|   ' * (level - 1), '|-- ', file)