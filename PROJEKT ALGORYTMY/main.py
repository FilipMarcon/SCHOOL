from timeit import timeit
from random import random
from heapify import *
from bubble import *
from merge import *
from quicksort import *

if __name__ == "__main__":
    random_arr = [int(random() * 10000 + 1) for _ in range(300000)]
    unsorted_arr = [i for i in range(300000, 1, -1)]
    sorted_arr = [i for i in range(1, 300000)]

    print('Random array:\n')
    print(f'MERGE SORT: {timeit(lambda: merge_sort(random_arr), number=1)}')
    #print(f'QUICK SORT: {timeit(lambda: quick_sort(random_arr, 0, len(random_arr) - 1), number=1)}\n')
    print(f'HEAP SORT: {timeit(lambda: heap_sort(random_arr), number=1)}')
    print(f'BUBBLE SORT: {timeit(lambda: bubble_sort(random_arr), number=1)}\n')

    print(f'Sorted array:')
    print(f'MERGE SORT: {timeit(lambda: merge_sort(sorted_arr), number=1)}')
    print(f'HEAP SORT: {timeit(lambda: heap_sort(sorted_arr), number=1)}')
    print(f'BUBBLE SORT: {timeit(lambda: bubble_sort(sorted_arr), number=1)}\n')

    print(f'Unsorted array:')
    print(f'MERGE SORT: {timeit(lambda: merge_sort(unsorted_arr), number=1)}')
    print(f'HEAP SORT: {timeit(lambda: heap_sort(unsorted_arr), number=1)}')
    print(f'BUBBLE SORT: {timeit(lambda: bubble_sort(unsorted_arr), number=1)}')



