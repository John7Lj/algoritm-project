import math
import time
import random

# Distance calculation
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Divide and Conquer - Helper Functions
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

# Generate random points
def generate_random_points(n):
    random.seed(42)  # For reproducibility
    return [(random.uniform(0, 1000), random.uniform(0, 1000)) for _ in range(n)]

# Performance testing
def measure_time(points, runs=5):
    """Measure average execution time over multiple runs"""
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        closest_pair(points)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)

# Main performance test
def run_optimized_performance_test():
    # Test sizes
    test_sizes = [100, 500, 1000, 2000]
    
    print("="*70)
    print("DIVIDE & CONQUER ALGORITHM - PERFORMANCE TEST")
    print("="*70)
    print(f"\n{'Input Size (n)':<20} {'Execution Time (s)':<25} {'Approx Operations':<20}")
    print("-"*70)
    
    results = []
    
    for n in test_sizes:
        # Generate test data
        points = generate_random_points(n)
        
        # Measure execution time
        exec_time = measure_time(points)
        
        # Approximate operations for O(n log n)
        operations = int(n * math.log2(n))
        
        # Store results
        results.append({
            'size': n,
            'time': exec_time,
            'operations': operations
        })
        
        # Print results
        print(f"{n:<20} {exec_time:<25.6f} {operations:<20,}")
    
    # Summary statistics
    print("\n" + "="*70)
    print("SUMMARY - DIVIDE & CONQUER ALGORITHM")
    print("="*70)
    
    print("\nExecution Times:")
    for r in results:
        print(f"  n={r['size']:<5} → {r['time']:.6f} seconds (~{r['operations']:,} operations)")
    
    print("\nTime Complexity Analysis:")
    print("  Algorithm: Divide and Conquer")
    print("  Time Complexity: O(n log n)")
    print("  Space Complexity: O(n)")
    
    print("\nGrowth Rate Verification:")
    for i in range(1, len(results)):
        time_ratio = results[i]['time'] / results[i-1]['time']
        size_ratio = results[i]['size'] / results[i-1]['size']
        expected_ratio = size_ratio * (math.log2(results[i]['size']) / math.log2(results[i-1]['size']))
        print(f"  n={results[i-1]['size']} → n={results[i]['size']}:")
        print(f"    Actual time ratio: {time_ratio:.2f}")
        print(f"    Expected O(n log n) ratio: {expected_ratio:.2f}")
    
    print("\n" + "="*70)

# Run the test
if __name__ == "__main__":
    run_optimized_performance_test()
