import os
import extcount
import stats
import directory_tree
import wget
import make_slug
import links
import csv2xls

if __name__ == '__main__':
    # Problem 58: Write a program to list all files in the given directory.
    print('list directory: ' + str(os.listdir()) + '\n')

    # Problem 59: Write a program extcount.py to count number of files for each extension in the given directory. The
    # program should take a directory name as argument and print count and extension for each available file extension.
    print('\nCOUNT:')
    extcount.extcount()

    # Problem 60: Write a program to list all the files in the given directory along with their length and last modification
    # time. The output should contain one line for each file containing filename, length and modification date separated
    # by tabs. Hint: see help for os.stat.
    print('\nSTATS:')
    stats.stats()

    # Problem 61: Write a program to print directory tree. The program should take path of a directory as argument
    # and print all the files in it recursively as a tree.
    print('\nDIRECTORY TREE:')
    directory = 'C:\AQ\Dark'
    print(os.path.basename(directory))
    directory_tree.directory_tree(directory)

    # Problem 62: Write a program wget.py to download a given URL. The program should accept a URL as argument,
    # download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as
    # index.html.
    print('\nwget: ')
    wget.wget('http://docs.python.org/tutorial/interpreter.html')
    wget.wget('http://docs.python.org/tutorial/')

    # Problem 64: Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces
    # and special characters are replaced by a hyphen, typically used to create blog post URL from post title. It should
    # also make sure there are no more than one hyphen in any place and there are no hyphens at the biginning and end
    # of the slug.
    print('\nmake_slug("hello world"): ', make_slug.make_slug("hello world"))
    print('make_slug("hello  world!"): ', make_slug.make_slug("hello  world!"))
    print('make_slug(" --hello-  world--"): ', make_slug.make_slug(" --hello-  world--"))
    print('make_slug("  -   --hello- +    world--   +"): ', make_slug.make_slug("  -   --hello- +    world--   +"))

    # Problem 65: Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked
    # from that webpage.
    links.links('http://docs.python.org/tutorial/interpreter.html')

    # Problem 70: Write a program csv2xls.py that reads a csv file and exports it as Excel file. The prigram should
    # take two arguments. The name of the csv file to read as first argument and the name of the Excel file to write as
    # the second argument.
    csv2xls.csv2xls('csv.csv', 'excel.xls')