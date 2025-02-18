import math
from insertion import insertion_sort
from heap import heapsort

def introspective_sort(arr: list[int]) -> list[int]:
    def introsort(arr: list[int], maxdepth: int) -> list[int]:
        if len(arr) < 5: # can be tuned based on input array
            return insertion_sort(arr)
        elif maxdepth == 0:
            return heapsort(arr)
        else:
            # quicksort
            pivot = len(arr) // 2
            i = 0
            while i < pivot:
                if arr[i] > arr[pivot]:
                    arr[i], arr[pivot - 1], arr[pivot] = arr[pivot - 1], arr[pivot], arr[i]
                    pivot -= 1
                    i -= 1
                i += 1
            i += 1
            while i < len(arr):
                if arr[i] < arr[pivot]:
                    arr[i], arr[pivot + 1], arr[pivot] = arr[pivot + 1], arr[pivot], arr[i]
                    pivot += 1
                    i -= 1
                i += 1
            return introsort(arr[:pivot], maxdepth - 1) + [arr[pivot]] + introsort(arr[pivot + 1:], maxdepth - 1)

    maxdepth = math.floor(math.log2(len(arr))) * 2 # can be tuned based on input array
    return introsort(arr, maxdepth)


if __name__ == '__main__':
    nums = [3, 5, 1, 2, 9, 4, 6, 8, 7, 0]
    print(introspective_sort(nums))