import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            min_dist = min(min_dist, distance(points[i], points[j]))
    return min_dist

def strip_closest(strip, d):
    min_dist = d
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            min_dist = min(min_dist, distance(strip[i], strip[j]))
    return min_dist

def closest_pair_rec(points_x, points_y):
    n = len(points_x)
    if n <= 3:
        return brute_force(points_x)
    
    mid = n // 2
    mid_point = points_x[mid]
    left_x = points_x[:mid]
    right_x = points_x[mid:]
    
    left_y = []
    right_y = []
    for p in points_y:
        if p[0] <= mid_point[0]:
            left_y.append(p)
        else:
            right_y.append(p)
    
    dl = closest_pair_rec(left_x, left_y)
    dr = closest_pair_rec(right_x, right_y)
    d = min(dl, dr)
    
    strip = [p for p in points_y if abs(p[0] - mid_point[0]) < d]
    return min(d, strip_closest(strip, d))

def closest_pair(points):
    points_x = sorted(points, key=lambda x: x[0])
    points_y = sorted(points, key=lambda x: x[1])
    return closest_pair_rec(points_x, points_y)

# Sample data
points = [
    (2, 3),
    (12, 30),
    (40, 50),
    (5, 1),
    (12, 10),
    (3, 4),
    (20, 25),
    (15, 18)
]

# Test the algorithm
min_distance = closest_pair(points)
print(f"The smallest distance between any two points is: {min_distance:.2f}")
print(f"Points: {points}")
