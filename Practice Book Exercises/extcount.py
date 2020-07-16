import os

# Problem 59: Write a program extcount.py to count number of files for each extension in the given directory. The
# program should take a directory name as argument and print count and extension for each available file extension.
def extcount():
    all_files = os.listdir()
    files_dict = {}
    for file in all_files:
        ext = file.split('.')[-1]
        files_dict[ext] = files_dict.get(ext, 0) + 1
    #list = sorted(list(files_dict.items()), key=lambda x:x[1], reverse=True)
    for item in sorted(list(files_dict.items()), key=lambda x:x[1], reverse=True):
        print(str(item[1]) + ' ' + str(item[0]))