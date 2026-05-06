"""Session 1 exercises: linear search, factorial, optimized bubble sort."""
from typing import List

def linear_search(lst: List[int], target: int) -> bool:
    for item in lst:
        if item == target:
            return True
    return False

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

def bubble_sort_optimized(a: List[int]) -> List[int]:
    n = len(a)
    arr = a[:]
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    print("linear_search([1,2,3], 2)", linear_search([1,2,3], 2))
    print("factorial(5)", factorial(5))
    print("bubble_sort_optimized([3,1,2])", bubble_sort_optimized([3,1,2]))
