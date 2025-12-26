import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair_naive(points):
    min_dist = float('inf')
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair, min_dist

# Test data
points = [
    (2, 3),
    (12, 30),
    (40, 50),
    (5, 1),
    (12, 10),
    (3, 4),
    (20, 25),
    (15, 18),
    (8, 7),
    (35, 42)
]

# Run the algorithm
pair, min_dist = closest_pair_naive(points)

# Display results
print(f"Points: {points}")
print(f"\nClosest pair: {pair[0]} and {pair[1]}")
print(f"Minimum distance: {min_dist:.4f}")
