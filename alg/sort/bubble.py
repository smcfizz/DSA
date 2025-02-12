from typing import List


def bubble_sort(arr: list[int]) -> List:
    '''
    Time complexity:    O(n^2)
    Space complexity:   O(1)
    Swaps:              O(n^2)
    Stable:             Yes
    '''
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    nums = [3, 5, 1, 2, 9, 4, 6, 8, 7, 0]
    print(bubble_sort(nums))