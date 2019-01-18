# Closest numbers problem:


# Check if given list is sorted.
def is_sorted(n):
    for i in range(len(n)):
        for j in range(i, len(n)):
            if n[i] > n[j]:
                return False
    return True


# If list isn't sorted, sort it by bubble sort.
def bubble_sort(n):

    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] > n[j]:
                n[i], n[j] = n[j], n[i]
    return n


# Find the closest pair.
def closest_pair(n):

    if len(n) < 2:
        return n
    else:
        dist = n[1] - n[0]
        num1, num2 = n[1], n[0]
        for i in range(0, len(n)-1):
            if (n[i+1] - n[i]) < dist:
                num1 = n[i]
                num2 = n[i+1]
                dist = num2 - num1

        return dist, num1, num2


numbers = [7, 54, 85, 36, 79, 21, 23, 49]
print("Our list:", numbers)

if is_sorted(numbers):
    print("List is already sorted")
else:
    numbers = bubble_sort(numbers)
    print(f"\nWe need to sort the list. \nSorted list:{numbers}")

if len(numbers) < 2:
    print(numbers, "This is the only one number on the list.")
else:
    result = closest_pair(numbers)
    print(f"\nThe closest pair is: {result[1]} and {result[2]}. The distance between is: {result[0]}")
