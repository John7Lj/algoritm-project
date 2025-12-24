import math
import time
import random

def distance(p1, p2):
    """Calculate Euclidean distance between two points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair_strip(strip, d):
    """
    Find the closest pair in a strip of points
    """
    min_dist = d
    closest_pair = None
    strip.sort(key=lambda point: point[1])  # Sort by y-coordinate
    
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (strip[i], strip[j])
            j += 1
    
    return closest_pair, min_dist

def closest_pair_recursive(px, py):
    """
    Recursive function using divide and conquer
    px: points sorted by x-coordinate
    py: points sorted by y-coordinate
    """
    n = len(px)
    
    # Base case: use brute force for small inputs
    if n <= 3:
        min_dist = float('inf')
        closest_pair = None
        for i in range(n):
            for j in range(i + 1, n):
                dist = distance(px[i], px[j])
                if dist < min_dist:
                    min_dist = dist
                    closest_pair = (px[i], px[j])
        return closest_pair, min_dist
    
    # Divide
    mid = n // 2
    midpoint = px[mid]
    
    pyl = [p for p in py if p[0] <= midpoint[0]]
    pyr = [p for p in py if p[0] > midpoint[0]]
    
    # Conquer
    left_pair, left_dist = closest_pair_recursive(px[:mid], pyl)
    right_pair, right_dist = closest_pair_recursive(px[mid:], pyr)
    
    # Find minimum of two sides
    if left_dist < right_dist:
        d = left_dist
        min_pair = left_pair
    else:
        d = right_dist
        min_pair = right_pair
    
    # Build strip array
    strip = [p for p in py if abs(p[0] - midpoint[0]) < d]
    
    # Find closest points in strip
    strip_pair, strip_dist = closest_pair_strip(strip, d)
    
    # Return the minimum
    if strip_dist < d:
        return strip_pair, strip_dist
    return min_pair, d

def closest_pair_optimized(points):
    """
    Optimized divide and conquer approach
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(points) < 2:
        return None, float('inf')
    
    px = sorted(points, key=lambda p: p[0])  # Sort by x
    py = sorted(points, key=lambda p: p[1])  # Sort by y
    
    return closest_pair_recursive(px, py)

def generate_random_points(n, max_coord=1000):
    """Generate n random points with coordinates in range [0, max_coord]"""
    return [(random.uniform(0, max_coord), random.uniform(0, max_coord)) for _ in range(n)]

def run_test(n):
    """Run a single test with n points and measure execution time"""
    points = generate_random_points(n)
    
    start_time = time.time()
    pair, dist = closest_pair_optimized(points)
    end_time = time.time()
    
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    
    return execution_time, pair, dist

if __name__ == "__main__":
    # Test with different input sizes
    test_sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000]
    
    print("="*60)
    print("Optimized Closest Pair Algorithm - Performance Testing")
    print("="*60)
    
    for size in test_sizes:
        exec_time, pair, dist = run_test(size)
        print(f"\nInput size: {size} points")
        print(f"Execution time: {exec_time:.4f} ms")
        print(f"Minimum distance: {dist:.4f}")
        if pair:
            print(f"Closest pair: {pair[0]} and {pair[1]}")