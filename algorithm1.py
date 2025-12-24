import math
import time
import random

def distance(p1, p2):
    """Calculate Euclidean distance between two points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair_naive(points):
    """
    Naive approach: Check all possible pairs of points
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(points)
    if n < 2:
        return None, float('inf')
    
    min_dist = distance(points[0],points[1])
    closest_pair =(points[0],points[1])
    
    # Check every possible pair
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
    
    return closest_pair, min_dist

def generate_random_points(n, max_coord=1000):
    """Generate n random points with coordinates in range [0, max_coord]"""
    return [(random.uniform(0, max_coord), random.uniform(0, max_coord)) for _ in range(n)]

def run_test(n):
    """Run a single test with n points and measure execution time"""
    points = generate_random_points(n)
    
    start_time = time.time()
    pair, dist = closest_pair_naive(points)
    end_time = time.time()
    
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    
    return execution_time, pair, dist

if __name__ == "__main__":
    # Test with different input sizes
    test_sizes = [10, 50, 100, 200, 500, 1000]
    
    print("="*60)
    print("Naive Closest Pair Algorithm - Performance Testing")
    print("="*60)
    
    for size in test_sizes:
        exec_time, pair, dist = run_test(size)
        print(f"\nInput size: {size} points")
        print(f"Execution time: {exec_time:.4f} ms")
        print(f"Minimum distance: {dist:.4f}")
        if pair:
            print(f"Closest pair: {pair[0]} and {pair[1]}")