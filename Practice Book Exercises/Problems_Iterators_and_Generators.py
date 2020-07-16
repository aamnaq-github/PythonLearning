import reverse_iter

if __name__ == '__main__':

    # Problem 76: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction.
    a = reverse_iter.reverse_iter([1, 2, 3, 4, 4, 5, 5])
    while True:
        print(a.next())