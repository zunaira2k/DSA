import random
import time
import matplotlib.pyplot as plt

# Quick Sort implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
 

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Generate one array of size 10000 with random values between 2000 and 10000
array_size = 10000
arr = [random.randint(200, 10000) for _ in range(array_size)]

sizes = list(range(1000, array_size + 1, 1000))
quick_sort_times = []
merge_sort_times = []

for size in sizes:
    subset = arr[:size]

    # Time Quick Sort
    start = time.time()
    quick_sort(subset)
    quick_sort_times.append(time.time() - start)

    # Time Merge Sort
    start = time.time()
    merge_sort(subset)
    merge_sort_times.append(time.time() - start)

    print(f"Size: {size} | Quick Sort: {quick_sort_times[-1]:.4f}s | Merge Sort: {merge_sort_times[-1]:.4f}s")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(sizes, quick_sort_times, marker='o', color='blue', label='Quick Sort')
plt.plot(sizes, merge_sort_times, marker='o', color='red', label='Merge Sort')
plt.title('Quick Sort vs Merge Sort Performance')
plt.xlabel('Number of Elements Sorted')
plt.ylabel('Time Taken (seconds)')
plt.legend()
plt.grid(True)
plt.show()
