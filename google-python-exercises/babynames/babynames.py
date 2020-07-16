#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  names_list = []
  file_read = open(filename, 'r')
  file_data = file_read.read()
  file_read.close()
  year = re.search(r'Popularity in (\d\d\d\d)', file_data).group(1)
  names_list.append(year)
  # Extract all the data tuples with a findall()
  # each tuple is: (rank, boy-name, girl-name)
  names = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', file_data)
  # Store data into a dict using each name as a key and that
  # name's rank number as the value.
  # (if the name is already in there, don't add it, since
  # this new rank will be bigger than the previous rank).
  names_to_rank = {}
  for name in names:
    (rank, boyname, girlname) = name
    if boyname not in names_to_rank:
      names_to_rank[boyname] = rank
    if girlname not in names_to_rank:
      names_to_rank[girlname] = rank
  sorted_names = sorted(names_to_rank.keys())
  for name in sorted_names:
    names_list.append(name + ' ' + names_to_rank[name])
  print(names_list)
  return names_list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  sys.argv.append('--summaryfile')
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  files = os.listdir('.')
  for file in files:
    if file.endswith('.html'):
      extracted_names = extract_names(file)
      file_read = open(file, 'r')
      file_data = file_read.read()
      file_read.close()
      year = re.search(r'Popularity in (\d\d\d\d)', file_data).group(1)
      print (year)
      outf = open('babynamesoutput' + year + '.txt', 'w')
      outf.write(str(extracted_names) + '\n\n')
      outf.write(year + '\n')
      # Extract all the data tuples with a findall()
      # each tuple is: (rank, boy-name, girl-name)
      names = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', file_data)
      names_dict = {}
      for name in names:
        print (name[0] + '\t\t' + name[1] + '\t\t' + name[2])
        (rank, boyname, girlname) = name
        names_dict[rank] = [boyname , girlname]
      print(names_dict)
      for entry in names_dict:
        outf.write(str(entry) + '\t' + str(names_dict[entry]) + '\n')
      outf.close()

if __name__ == '__main__':
  main()
