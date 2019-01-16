# Merge Sorting.


import random

def array_gen(length = 4, volume = 50):
    array = []
    for i in range(length):
        array.append((random.randint(0, volume)))
    return array


def merge(a, b):

    c = []
    a_ind, b_ind = 0, 0
    while a_ind < len(a) and b_ind < len(b):
        if a[a_ind] < b[b_ind]:
            c.append(a[a_ind])
            a_ind += 1
        else:
            c.append(b[b_ind])
            b_ind += 1

    c.extend(b[b_ind:])
    c.extend(a[a_ind:])

    return c

i = 0

def merge_sort(x):

    if len(x) <= 1:
        return x

    left = merge_sort(x[:len(x)//2])
    print(i, left)
    right = merge_sort(x[len(x)//2:])
    print(i, right)

    return merge(left, right)


new_arrray = array_gen()
print(new_arrray)
a = [1, 3, 6]
b = [2, 4, 7]

s = merge_sort(new_arrray)
print(s)

