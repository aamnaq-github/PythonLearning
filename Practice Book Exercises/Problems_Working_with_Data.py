import random

# Problem 12: Write a function count_digits to find number of digits in the given number.
def count_digits(number):
    return len(number)

# Problem 13: Write a function istrcmp to compare two strings, ignoring the case.
def istrcmp(str1, str2):
    return str1.lower() == str2.lower()

# Problem 21: Python has a built-in function sum to find sum of all elements of a list. Provide an implementation
# for sum.
def sum_list(num_list):
    sum = 0
    for num in num_list:
        sum = sum + num
    print ('Sum = %d' %sum)

# Problem 22: What happens when the above sum function is called with a list of strings? Can you make your sum
# function work for a list of strings as well.
def sum_list_strings():
    strings_list = []
    for i in range(2):
        strings_list.append(input('Enter a string: '))
    sum = ''
    for string in strings_list:
        sum = sum + string
    print('Sum = ' + sum + '\n')

# Problem 23: Implement a function product, to compute product of a list of numbers.
def product(num_list):
    product = 1
    for num in num_list:
        product = product * num
    return product

# Problem 24: Write a function factorial to compute factorial of a number. Can you use the product function
# defined in the previous example to compute factorial?
def factorial(num):
    factorial = 1
    for i in range(1,num+1):
        factorial = product([factorial, i])
    return factorial

# Problem 27: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a
# function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of
# strings?
def cumulative_sum(char_list):
    cumulative_sum = [char_list[0]]
    index = 0
    for char in char_list[1:]:
        cumulative_sum.append(cumulative_sum[index] + '+' + char)
        index += 1
    return cumulative_sum

# Problem 28: Write a function cumulative_product to compute cumulative product of a list of numbers.
def cumulative_product(num_list):
    cumulative_product = [num_list[0]]
    index = 0
    for num in num_list[1:]:
        cumulative_product.append(product([cumulative_product[index], num]))
        index += 1
    return cumulative_product

# Problem 29: Write a function unique to find all the unique elements of a list.
def unique(num_list):
    unique_list = []
    for num in num_list:
        if not unique_list.__contains__(num):
            unique_list.append(num)
    return unique_list

# Problem 30: Write a function dups to find all duplicates in the list.
def dups(num_list):
    duplicates_list = []
    index = 0
    for num in num_list:
        for rest_num in num_list[index + 1:]:
            if num == rest_num and not duplicates_list.__contains__(num):
                duplicates_list.append(num)
        index += 1
    return duplicates_list

# Problem 31: Write a function group(list, size) that take a list and splits into smaller lists of given size.
def group(list, size):
    groups_list = []
    group_index = 0
    for i in range(0, size):
        start_index = group_index * size
        end_index = min(start_index + size, len(list))
        groups_list.append(list[start_index : end_index])
        group_index += 1
        if end_index == len(list):
            break
    return groups_list

# Problem 32: Write a function lensort to sort a list of strings based on length.
def lensort(list):
    return sorted(list, key=lambda x:len(x))

# Problem 33: Improve the unique function written in previous problems to take an optional key function as argument
# and use the return value of the key function to check for uniqueness.
def unique_improved(list, key):
    unique_list = []
    for item in list:
        if not unique_list.__contains__(key(item)):
            unique_list.append(item)
    return unique_list

# Problem 35: Write a function extsort to sort a list of files based on extension.
def extsort(list_of_files):
    return sorted(list_of_files, key=lambda x:x[x.index('.')+1])

# Problem 36: Write a program reverse.py to print lines of a file in reverse order.
def reverse(filename):
    file = open(filename, 'r')
    file_lines = file.readlines()
    for i in range(len(file_lines), 0, -1):
        print(file_lines[i-1].replace('\n', ''))
    file.close()

# Problem 40: Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer
# than width.
def wrap(filename, width):
    file = open(filename, 'r')
    file_lines = file.readlines()
    for i in range(len(file_lines), 0, -1):
        print(file_lines[i - 1].replace('\n', '')[:width] + '\n' + file_lines[i - 1].replace('\n', '')[width:])
    file.close()

# Problem 41: The above wrap program is not so nice because it is breaking the line at middle of any word. Can
# you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?
def wordwrap(filename, width):
    file = open(filename, 'r')
    file_lines = file.readlines()
    for i in range(len(file_lines), 0, -1):
        if (file_lines[i - 1].replace('\n', '')[width-1] == ' '):
            print(file_lines[i - 1].replace('\n', '')[:width] + '\n' + file_lines[i - 1].replace('\n', '')[width:])
        else:
            break_index = file_lines[i - 1].rindex(' ', 0, width)
            print(file_lines[i - 1].replace('\n', '')[:break_index+1] + '\n' + file_lines[i - 1].replace('\n', '')[break_index+1:])
    file.close()

# Problem 42: Write a program center_align.py to center align all lines in the given file.
def center_align(filename):
    file = open(filename, 'r')
    file_lines = file.readlines()
    for i in range(len(file_lines), 0, -1):
        spaces = int((140 - len(file_lines[i-1].replace('\n', '')))/2)
        print(' '*spaces + file_lines[i-1].replace('\n', '') + ' '*spaces)
    file.close()

# Problem 43: Provide an implementation for zip function using list comprehensions.
def zip_custom(list1, list2):
    return [(x, y) for x, y in zip(list1, list2)]

# Problem 44: Python provides a built-in function map that applies a function to each element of a list. Provide an
# implementation for map using list comprehensions.
def map_custom(function, range):
    return [function(range_item) for range_item in range]

# Problem 45: Python provides a built-in function filter(f, a) that returns items of the list a for which
# f(item) returns true. Provide an implementation for filter using list comprehensions.
def filter_custom(function, range):
    return [range_item for range_item in range if function(range_item)]

# Problem 46: Write a function triplets that takes a number n as argument and returns a list of triplets such
# that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a,
# b, c) and (b, a, c) represent same triplet.
def triplets(num):
    triplets = [(x, y, z) for x in range(1, num) for y in range(1, num) for z in range(1, num) if x + y == z]
    duplicate_triplets = []
    for i in range(0, len(triplets)):
        for j in range(i+1, len(triplets)):
            if triplets[i][2] == triplets[j][2] and triplets[i][0] == triplets[j][1]:
                duplicate_triplets.append(triplets[j])
    for duplicate_triplet in duplicate_triplets:
        triplets.remove(duplicate_triplet)
    return triplets

# Problem 47: Write a function enumerate that takes a list and returns a list of tuples containing
# (index,item) for each item in the list.
def enumerate_custom(list):
    enumerate_list = []
    index = range(len(list))
    enumerate_list = tuple(zip(index, list))
    return [(index, list) for index, list in enumerate_list]

# Problem 48: Write a function array to create an 2-dimensional array. The function should take both dimensions
# as arguments. Value of each element can be initialized to None:
def array(rows, columns):
    two_dimensional_array = [[None] * columns] * rows
    return two_dimensional_array

# Problem 49: Write a python function parse_csv to parse csv (comma separated values) files.
# Problem 50: Generalize the above implementation of csv parser to support any delimiter and comments.
def parse_csv(filename, delimiter, comments):
    file = open(filename, 'r')
    parsed = []
    for line in file.readlines():
        if not line.startswith(comments):
            parts = line.replace('\n', '').split(delimiter)
            parsed.append(parts)
    file.close()
    return parsed

# Problem 51: Write a function mutate to compute all words generated by a single mutation on a given word. A
# mutation is defined as inserting a character, deleting a character, replacing a character, or swapping 2 consecutive
# characters in a string. For simplicity consider only letters from a to z.
def mutate(word):
    mutate_list = [word]
    i = 0
    length = len(word)

    # inserting a character
    for i in range(0, length):
        for letter in list(map(chr, range(97, 123))):
            # inserting a character
            new_word = word[:i] + letter + word[i:]
            if new_word not in mutate_list:
                mutate_list.append(new_word)

            # replacing a character
            new_word = word[:i] + letter + word[i+1:]
            if new_word not in mutate_list:
                mutate_list.append(new_word)

        # deleting a character
        new_word = word[:i] + word[i + 1:]
        if new_word not in mutate_list:
            mutate_list.append(new_word)

        # swapping two consecutive characters
        if i+2 < length:
            new_word = word[:i] + word[i+1] + word[i] + word[i+2:]
            if new_word not in mutate_list:
                mutate_list.append(new_word)

    return sorted(mutate_list)

# Problem 52: Write a function nearly_equal to test whether two strings are nearly equal. Two strings a and
# b are nearly equal when a can be generated by a single mutation on b.
def nearly_equal(word1, word2):
    return word1 in mutate(word2)

# Problem 53: Improve the above program to print the words in the descending order of the number of occurrences.
def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency

def read_words(filename):
    return open(filename).read().split()

def words_desc_freq(filename):
    frequency = word_frequency(read_words(filename))
    result = sorted(frequency.items(), key=lambda x:x[1])
    return result

# Problem 54: Write a program to count frequency of characters in a given file. Can you use character frequency
# to tell whether the given file is a Python program file, C program file or a text file?
def characters_frequency(filename):
    frequency = {}
    python = ['print', 'def', 'items()', 'import']
    c = ['printf', 'scanf', '#include', '<stdio.h>']
    file_type = {'python':0, 'c':0}
    words = open(filename).read().split()
    for w in words:
        for char in w.lower():
            frequency[char] = frequency.get(char, 0) + 1
        if w in python:
            file_type['python'] = file_type.get('python', 0) + 1
        if w in c:
            file_type['c'] = file_type.get('c', 0) + 1
    if file_type['python'] == 0 and file_type['c'] > 0:
        print('It is a C program file.')
    elif file_type['c'] == 0 and file_type['python'] > 0:
        print('It is a Python program file.')
    else:
        print('It is a text file.')
    result = sorted(frequency.items(), key=lambda x:x[1])
    return result

# Problem 55: Write a program to find anagrams in a given list of words. Two words are called anagrams if one
# word can be formed by rearranging letters of another. For example ‘eat’, ‘ate’ and ‘tea’ are anagrams.
def anagrams(list_of_words):
    anagrams = []
    grouped_words = []
    for word in list_of_words:
        if word not in grouped_words:
            group = []
            group.append(word)
            grouped_words.append(word)
            for w in list_of_words:
                if w not in grouped_words:
                    if word.__sizeof__() == w.__sizeof__():
                        for char in w:
                            if not word.__contains__(char):
                                anagram = False
                                break
                            anagram = True
                        if anagram:
                            group.append(w)
                            grouped_words.append(w)
            anagrams.append(group)
    return anagrams

# Problem 56: Write a function valuesort to sort values of a dictionary based on the key.
def valuesort(dict):
    result = []
    sort = sorted(dict.items(), key=lambda x:x[0])
    for item in sort:
        result.append(item[1])
    return result

# Problem 57: Write a function invertdict to interchange keys and values in a dictionary. For simplicity,
# assume that all values are unique.
def invertdict(dict):
    result_dict = {}
    for item in dict:
        result_dict[dict[item]] = item
    return result_dict

if __name__ == '__main__':
    # Problem 12: Write a function count_digits to find number of digits in the given number.
    number = str(random.randrange(10, 100000))
    print('There are %d digits in %s.\n' %(count_digits(number), number))

    # Problem 13: Write a function istrcmp to compare two strings, ignoring the case.
    print('The strings \'Aamna\' and \'Qamar\' are same: ' + str(istrcmp('Aamna', 'Qamar')) + '\n')

    # Problem 21: Python has a built-in function sum to find sum of all elements of a list. Provide an implementation
    # for sum.
    num_list = []
    for i in range(5):
        num_list.append(random.randrange(1, 10))
    print('Numbers List: ' + str(num_list))
    sum_list(num_list)

    # Problem 23: Implement a function product, to compute product of a list of numbers.
    print('Product = %d\n' %product(num_list))

    # Problem 24: Write a function factorial to compute factorial of a number. Can you use the product function
    # defined in the previous example to compute factorial?
    number = random.randrange(1, 10)
    print('%d! = %d\n' %(number, factorial(number)))

    # Problem 27: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a
    # function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of
    # strings?
    char_list = ['Aamna', 'Qamar', 'is', 'an', 'ambidextrous']
    print('Cumulative sum of %s is %s\n' %(str(char_list), str(cumulative_sum(char_list))))

    # Problem 28: Write a function cumulative_product to compute cumulative product of a list of numbers.
    print('Cumulative product of %s is %s\n' % (str(num_list), str(cumulative_product(num_list))))

    # Problem 29: Write a function unique to find all the unique elements of a list.
    print('Unique elements of [1, 2, 1, 3, 2, 5] are %s\n' % str(unique([1, 2, 1, 3, 2, 5])))

    # Problem 30: Write a function dups to find all duplicates in the list.
    print('Duplicate elements of [1, 2, 1, 3, 2, 5] are %s\n' % str(dups([1, 2, 1, 3, 2, 5])))

    # Problem 31: Write a function group(list, size) that take a list and splits into smaller lists of given size.
    print('Groups list of group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) is %s' % str(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)))
    print('Groups list of group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4) is %s\n' % str(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)))

    # Problem 32: Write a function lensort to sort a list of strings based on length.
    print('lensort([\'python\', \'perl\', \'java\', \'c\', \'haskell\', \'ruby\']) = \n%s\n'
          %str(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])))

    # Problem 33: Improve the unique function written in previous problems to take an optional key function as argument
    # and use the return value of the key function to check for uniqueness.
    print('unique_improved(["python", "java", "Python", "Java"], key=lambda s: s.lower()) = \n%s\n'
          %str(unique_improved(["python", "java", "Python", "Java"], key=lambda s: s.lower())))

    # Problem 35: Write a function extsort to sort a list of files based on extension.
    print('extsort([\'a.c\', \'a.py\', \'b.py\', \'bar.txt\', \'foo.txt\', \'x.c\']) = \n%s\n'
          %str(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])))

    # Problem 36: Write a program reverse.py to print lines of a file in reverse order.
    print('REVERSED:')
    reverse('cat.txt')
    print('\n')

    # Problem 40: Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer
    # than width.
    print('WRAPPED:')
    wrap('cat.txt', 30)
    print('\n')

    # Problem 41: The above wrap program is not so nice because it is breaking the line at middle of any word. Can
    # you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?
    print('WORDWRAPPED:')
    wordwrap('cat.txt', 30)
    print('\n')

    # Problem 42: Write a program center_align.py to center align all lines in the given file.
    print('CENTER ALIGN:')
    center_align('cat.txt')
    print('\n')

    # Problem 43: Provide an implementation for zip function using list comprehensions.
    print('zip([1, 2, 3], ["a", "b", "c"]) = ' + str(zip_custom([1, 2, 3], ["a", "b", "c"])).replace('\'', '"') + '\n')

    # Problem 44: Python provides a built-in function map that applies a function to each element of a list. Provide an
    # implementation for map using list comprehensions.
    def square(x):
        return x * x
    def cube(x):
        return x * x * x
    print('map(square, range(10)) = ' + str(map_custom(square, range(10))))
    print('map(cube, range(10)) = ' + str(map_custom(cube, range(10))))

    # Problem 45: Python provides a built-in function filter(f, a) that returns items of the list a for which
    # f(item) returns true. Provide an implementation for filter using list comprehensions.
    def even(x):
        return x % 2 == 0
    print('\nfilter(even, range(10)) = ' + str(filter_custom(even, range(10))))

    # Problem 46: Write a function triplets that takes a number n as argument and returns a list of triplets such
    # that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a,
    # b, c) and (b, a, c) represent same triplet.
    print('\ntriplets(5) = ' + str(triplets(5)))
    
    # Problem 47: Write a function enumerate that takes a list and returns a list of tuples containing
    # (index,item) for each item in the list.
    print('\nenumerate(["a", "b", "c"]) = ' +
          str(tuple((index, value) for index, value in enumerate_custom(["a", "b", "c"]))).replace('\'', '"'))

    # Problem 48: Write a function array to create an 2-dimensional array. The function should take both dimensions
    # as arguments. Value of each element can be initialized to None:
    rows = random.randrange(1, 10)
    columns = random.randrange(1, 10)
    print('\narray(%d, %d) = ' %(rows, columns) + str(array(rows, columns)))

    # Problem 49: Write a python function parse_csv to parse csv (comma separated values) files.
    # Problem 50: Generalize the above implementation of csv parser to support any delimiter and comments.
    print('\nparse_csv(\'csv.csv\', \'!\', \'#\'): ' + str(parse_csv('csv.csv', '!', '#')))

    # Problem 51: Write a function mutate to compute all words generated by a single mutation on a given word. A
    # mutation is defined as inserting a character, deleting a character, replacing a character, or swapping 2 consecutive
    # characters in a string. For simplicity consider only letters from a to z.
    mutations = mutate('hello')
    print('\nmutate(\'hello\'): \n' + str(mutations))
    print('\'helo\' in mutations: ' + str('helo' in mutations))
    print('\'cello\' in mutations: ' + str('cello' in mutations))
    print('\'helol\' in mutations: ' + str('helol' in mutations))
    print('\'chello\' in mutations: ' + str('chello' in mutations))
    print('\'ehllo\' in mutations: ' + str('ehllo' in mutations))

    # Problem 52: Write a function nearly_equal to test whether two strings are nearly equal. Two strings a and
    # b are nearly equal when a can be generated by a single mutation on b.
    print('nearly_equal(\'python\', \'perl\'): ' + str(nearly_equal('python', 'perl')))
    print('nearly_equal(\'perl\', \'pearl\'): ' + str(nearly_equal('perl', 'pearl')))
    print('nearly_equal(\'python\', \'jython\'): ' + str(nearly_equal('python', 'jython')))
    print('nearly_equal(\'man\', \'woman\'): ' + str(nearly_equal('man', 'woman')))

    # Problem 53: Improve the above program to print the words in the descending order of the number of occurrences.
    print('\nWords in file in the descending order of the number of occurrences: ')
    print(words_desc_freq('cat.txt'))

    # Problem 54: Write a program to count frequency of characters in a given file. Can you use character frequency
    # to tell whether the given file is a Python program file, C program file or a text file?
    print('\nFrequency of characters in file: ')
    print(characters_frequency('cat.txt'))

    # Problem 55: Write a program to find anagrams in a given list of words. Two words are called anagrams if one
    # word can be formed by rearranging letters of another. For example ‘eat’, ‘ate’ and ‘tea’ are anagrams.
    print('\nanagrams([\'eat\', \'ate\', \'done\', \'tea\', \'soup\', \'node\']) = ' + str(anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])))

    # Problem 56: Write a function valuesort to sort values of a dictionary based on the key.
    print('\nvaluesort({\'x\': 1, \'y\': 2, \'a\': 3}) = ' + str(valuesort({'x': 1, 'y': 2, 'a': 3})))

    # Problem 57: Write a function invertdict to interchange keys and values in a dictionary. For simplicity,
    # assume that all values are unique.
    print('\ninvertdict({\'x\': 1, \'y\': 2, \'z\': 3}) = ' + str(invertdict({'x': 1, 'y': 2, 'z': 3})))