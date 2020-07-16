import os
import math
import dirtree

def exp(x, n):
    if n == 0:
        return 1
    else:
        return x * exp(x, n-1)

def fast_exp(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_exp(x*x, n/2)
    else:
        return x * fast_exp(x, n-1)

# Problem 86: Implement a function product to multiply 2 numbers recursively using + and - operators only.
def product(a, b):
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    if b == 1:
        return a
    return a + product(a, b-1)

# Problem 87: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character
def flatten_dict(dict):
    result = {}
    for item in dict:
        val = dict[item]
        if isinstance(val, type(dict)):
            temp = {}
            for x in val:
                temp[str(item) + '.' + str(x)] = val[x]
            result.update(flatten_dict(temp))
        else:
            result[item] = val
    return result

# Problem 88: Write a function unflatten_dict to do reverse of flatten_dict.
def unflatten_dict(dict):
    result = {}
    temp = {}
    for item in dict:
        val = dict[item]
        if item.__contains__('.'):
            keys = item.split('.')
            temp[keys[1]] = val
            result[keys[0]] = temp
        else:
            result[item] = val
    return result

# Problem 89: Write a function treemap to map a function over nested list.
def treemap(function, list):
    result = []
    for item in list:
        if isinstance(item, type(list)):
            result.append(treemap(function, item))
        else:
            result.append(function(item))
    return result

# Problem 90: Write a function tree_reverse to reverse elements of a nested-list recursively.
def tree_reverse(list):
    result = []
    for i in range(len(list), 0, -1):
        temp = list[i-1]
        if isinstance(temp, type(list)):
            result.append(tree_reverse(temp))
        else:
            result.append(list[i-1])
    return result

# Problem 91: Complete the above implementation of json_encode by handling the case of dictionaries.
def json_encode(data):
    if isinstance(data, bool):
        if data:
            return "true"
        else:
            return "false"
    elif isinstance(data, (int, float)):
        return str(data)
    elif isinstance(data, str):
        return '"' + escape_string(data) + '"'
    elif isinstance(data, list):
        return "[" + ", ".join(json_encode(d) for d in data) + "]"
    elif isinstance(data, dict):
        return "{" + ", ".join(json_encode(d)+':'+json_encode(i) for d,i in data.items()) + "}"
    else:
        raise TypeError("%s is not JSON serializable" % repr(data))

def escape_string(s):
    """Escapes double-quote, tab and new line characters in a string."""
    s = s.replace('"', '\\"')
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s

# Problem 93: Write a function count_change to count the number of ways to change any given amount.
# Available coins are also passed as argument to the function.
def count_change(amount, available_coins_list):
    if amount == 0:
        return 1
    elif amount < 0 or not available_coins_list:
        return 0
    else:
        return count_change(amount, available_coins_list[1:]) + count_change(amount-available_coins_list[0], available_coins_list)

# Problem 94: Write a function permute to compute all possible permutations of elements of a given list.
def permute(list):
    permutations = []
    size = len(list)
    if size == 0:
        return []
    if size == 1:
        return [list]
    for i in range(size):
        perm = list[i]
        temp = list[:i] + list[i+1:]
        for p in permute(temp):
            permutations.append([perm] + p)
    return permutations

# closure function
def outer_function(message):

    def inner_function():
        print(message)

    return inner_function

# decorator function
def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):
        print('\'wrapper\' executed this before \'{}\' function'.format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function

@decorator_function
def display():
    print('\'display\' function ran')

@decorator_function
def display_info(name, age):
    print('\'display_info\' ran with arguments ({}, {})'.format(name, age))

if __name__ == '__main__':
    # exponent of a number
    print('exp(2, 4):', exp(2, 4))

    # fast exponent using successive squaring
    print('fast_exp(2, 10):', fast_exp(2, 10))

    # Problem 86: Implement a function product to multiply 2 numbers recursively using + and - operators only.
    print('product(2, 24):', product(2, 24))

    # Problem 87: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character
    print('flatten_dict({\'a\': 1, \'b\': {\'x\': 2, \'y\': 3}, \'c\': 4}):\t', flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))

    # Problem 88: Write a function unflatten_dict to do reverse of flatten_dict.
    print('unflatten_dict({\'a\': 1, \'b.x\': 2, \'b.y\': 3, \'c\': 4}):\t', unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))

    # Problem 89: Write a function treemap to map a function over nested list.
    print('treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]):\t', treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]))

    # Problem 90: Write a function tree_reverse to reverse elements of a nested-list recursively.
    print('tree_reverse([[1, 2], [3, [4, 5]], 6]):\t', tree_reverse([[1, 2], [3, [4, 5]], 6]))

    # Problem 91: Complete the above implementation of json_encode by handling the case of dictionaries.
    print('json_encode([1,2,3]):\t', json_encode([1,2,3]))
    print('json_encode({\'a\':True,\'b\':2}):\t', json_encode({'a':True,'b':2}))

    # Problem 92: Implement a program dirtree.py that takes a directory as argument and prints all the files in that
    # directory recursively as a tree. Hint: Use os.listdir and os.path.isdir funtions.
    dir = 'C:\AQ\Dark'
    print('\ndir(\'', dir, '\'):')
    print(os.path.basename(dir))
    dirtree.dirtree(dir)

    # Problem 93: Write a function count_change to count the number of ways to change any given amount.
    # Available coins are also passed as argument to the function.
    print('\ncount_change(10, [1, 5]):', count_change(10, [1, 5]))
    print('count_change(10, [1, 2]):', count_change(10, [1, 2]))
    print('count_change(100, [1, 5, 10, 25, 50]):', count_change(100, [1, 5, 10, 25, 50]))

    # Problem 94: Write a function permute to compute all possible permutations of elements of a given list.
    print('\npermute([1, 2, 3]):', permute([1, 2, 3]))

    # closure function
    print('\nClosure Function: ')
    hi_func = outer_function('Hi')
    bye_func = outer_function('Bye')
    hi_func()
    bye_func()

    # decorator:
    # a function that takes another function as an argument,
    # adds some kind of functionality,
    # and then returns another function,
    # all of this without altering the source code of the original function passed in.
    print('\nDecorator Function: ')
    display()
    display_info('John', 25)