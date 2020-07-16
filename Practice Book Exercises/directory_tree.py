import os

# Problem 61: Write a program to print directory tree. The program should take path of a directory as argument
# and print all the files in it recursively as a tree.
def directory_tree(directory, level = 1):
    all_files = os.listdir(directory)
    if level > 1:
        if level-2 == 0:
            print('|-- ', os.path.basename(directory))
        else:
            print('|  ' * (level-2), '|-- ', os.path.basename(directory))
    for file in all_files:
        if not os.path.isfile(directory + '/' + file):
            directory_tree(directory+'\\'+file, level+1)
        else:
            if all_files[-1] == file:
                print('|   ' * (level - 1), '\-- ', file)
            else:
                print('|   ' * (level-1), '|-- ', file)
