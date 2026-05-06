"""Session 4 exercise: multiprocessing factorial and Pool example."""
import multiprocessing
from functools import reduce

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def compute_factorial_list(numbers):
    with multiprocessing.Pool() as pool:
        return pool.map(factorial, numbers)

def sum_of_squares(sublist):
    return sum(x * x for x in sublist)

def chunked_sum_of_squares(numbers, chunks=4):
    size = max(1, len(numbers) // chunks)
    sublists = [numbers[i:i+size] for i in range(0, len(numbers), size)]
    with multiprocessing.Pool() as pool:
        return sum(pool.map(sum_of_squares, sublists))

if __name__ == "__main__":
    nums = [5,6,7,8]
    print("factorials:", compute_factorial_list(nums))
    print("sum of squares:", chunked_sum_of_squares(list(range(1,21)), chunks=4))
