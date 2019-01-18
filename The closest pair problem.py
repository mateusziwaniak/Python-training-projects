# The closest pair of points problem.
import math


# Count distance, between all points and put it into dictionary.
def count_distance(n):
    dist_array = {}
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            x = int(math.fabs(n[i][0] - n[j][0]))
            y = int(math.fabs(n[i][1] - n[j][1]))
            dist = round(math.sqrt(x**2 + y**2), 2)
            dist_array.update([((n[i], n[j]), dist)])

    return dist_array


points = [(1, 2), (5, 6), (0, 4), (1, 1), (2, 7)]
distance = count_distance(points)
print(f"This is dictionary of points and distances between them: {distance}")

x = min(distance, key=distance.get) # Choose the smallest distance and set item of dict as x.
print(x)

print(f"The closes pair of points is point: {x[0]}, and point: {x[1]}. The distance is {min(distance.values())}.")
