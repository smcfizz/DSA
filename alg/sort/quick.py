from typing import List


def quicksort(arr: list[int]) -> List:
    '''
    Time complexity:    O(n log n)
    Space complexity:   O(log n)
    Swaps:              O(n log n) on average
    Stable:             Yes
    '''
    if len(arr) < 2:
        return arr
    
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
    
    return quicksort(arr[:pivot]) + arr[pivot:pivot + 1] + quicksort(arr[pivot + 1:])


if __name__ == "__main__":
    nums = [3, 5, 1, 2, 9, 4, 6, 8, 7, 0]
    print(quicksort(nums))