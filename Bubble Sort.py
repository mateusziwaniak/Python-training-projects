# Bubble sort


def bubbe_sort(list_to_sort):

    j = len(list_to_sort)-1

    while j:

        for i in range(j):

            if list_to_sort[i] > list_to_sort[i+1]:
                list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]

        j -= 1
        print(list_to_sort)
    return list_to_sort


numbers = [100, 7, 5, 1, 9, 4, 7, 2, 1, 10, 3, 1]

sorted_list = bubbe_sort(numbers)
print(sorted_list)
