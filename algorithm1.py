import math
import time
import random

# Distance calculation
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Naive Algorithm
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

# Generate random points
def generate_random_points(n):
    random.seed(42)  
    return [(random.uniform(0, 1000), random.uniform(0, 1000)) for _ in range(n)]

# Performance testing
def measure_time(points, runs=5):

    times = []
    for _ in range(runs):
        start = time.perf_counter()
        closest_pair_naive(points)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)

# Main performance test
def run_naive_performance_test():
    # Test sizes
    test_sizes = [100, 500, 1000, 2000]
    
    print("="*70)
    print("NAIVE ALGORITHM - PERFORMANCE TEST")
    print("="*70)
    print(f"\n{'Input Size (n)':<20} {'Execution Time (s)':<25} {'Comparisons':<20}")
    print("-"*70)
    
    results = []
    
    for n in test_sizes:
        # Generate test data
        points = generate_random_points(n)
        
        # Measure execution time
        exec_time = measure_time(points)
        
        # Calculate number of comparisons
        comparisons = n * (n - 1) // 2
        
        # Store results
        results.append({
            'size': n,
            'time': exec_time,
            'comparisons': comparisons
        })
        
        # Print results
        print(f"{n:<20} {exec_time:<25.6f} {comparisons:<20,}")
    
    # Summary statistics
    print("\n" + "="*70)
    print("SUMMARY - NAIVE ALGORITHM")
    print("="*70)
    
    print("\nExecution Times:")
    for r in results:
        print(f"  n={r['size']:<5} → {r['time']:.6f} seconds ({r['comparisons']:,} comparisons)")
    
    print("\nTime Complexity Analysis:")
    print("  Algorithm: Brute Force (Naive)")
    print("  Time Complexity: O(n²)")
    print("  Space Complexity: O(1)")
    
    print("\nGrowth Rate Verification:")
    for i in range(1, len(results)):
        time_ratio = results[i]['time'] / results[i-1]['time']
        size_ratio = results[i]['size'] / results[i-1]['size']
        expected_ratio = size_ratio ** 2
        print(f"  n={results[i-1]['size']} → n={results[i]['size']}:")
        print(f"    Actual time ratio: {time_ratio:.2f}")
        print(f"    Expected O(n²) ratio: {expected_ratio:.2f}")
    
    print("\n" + "="*70)

# Run the test
if __name__ == "__main__":
    run_naive_performance_test()
