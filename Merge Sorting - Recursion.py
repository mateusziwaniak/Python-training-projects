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


def merge_sort(x):

    if len(x) <= 1:
        return x

    left = merge_sort(x[:len(x)//2])
    right = merge_sort(x[len(x)//2:])

    return merge(left, right)


new_arrray = array_gen()
print(new_arrray)

s = merge_sort(new_arrray)
print(s)

