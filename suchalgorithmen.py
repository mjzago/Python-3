# from abc import ABC, abstractmethod


# class Search(ABC):
#     def __init__(self, array):
#         self.array = array
#         pass

#     @abstractmethod
#     def search(self, target):
#         pass

#     @abstractmethod
#     def set_array(self, array):
#         pass


# class LinearSearch(Search):
#     def search(self, target):
#         # add your code
#         pass

#     def set_array(self, array):
#         # add your code
#         pass


# class BinarySearch(Search):
#     def search(self, target):
#         # add your code
#         pass

#     def set_array(self, array):
#         # add your code
#         pass


# # Then generates large sorted lists and tests the runtime of the binary search with lists of different sizes.   




import time
import random

class LinearSearch(Search):
    def search(self, target):
        for index, value in enumerate(self.array):
            if value == target:
                return index
        return -1  # Not found

    def set_array(self, array):
        self.array = array


class BinarySearch(Search):
    def search(self, target):
        left, right = 0, len(self.array) - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_value = self.array[mid]

            if mid_value == target:
                return mid
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1  # Not found

    def set_array(self, array):
        self.array = array


# Function to generate a sorted list of given size
def generate_sorted_list(size):
    return sorted([random.randint(0, 10000) for _ in range(size)])

# Testing the runtime of binary search with lists of different sizes
list_sizes = [100, 1000, 10000, 100000]
target = 42  # Target value to search for

for size in list_sizes:
    sorted_list = generate_sorted_list(size)

    linear_search = LinearSearch(sorted_list)
    binary_search = BinarySearch(sorted_list)

    start_time = time.time()
    linear_search.search(target)
    linear_search_time = time.time() - start_time

    start_time = time.time()
    binary_search.search(target)
    binary_search_time = time.time() - start_time

    print(f"List size: {size}")
    print(f"Linear Search Time: {linear_search_time:.6f} seconds")
    print(f"Binary Search Time: {binary_search_time:.6f} seconds")
    print("-" * 30)
