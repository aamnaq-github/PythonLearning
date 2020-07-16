import os
import time

# Problem 60: Write a program to list all the files in the given directory along with their length and last modification
# time. The output should contain one line for each file containing filename, length and modification date separated
# by tabs. Hint: see help for os.stat.
def stats():
    all_files = os.listdir()
    for file in all_files:
        stats = os.stat(os.getcwd() + '/' + file)
        print(file, '\t'*2, stats.st_size, '\t'*2, time.ctime(stats.st_mtime))
