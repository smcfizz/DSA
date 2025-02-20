def insertion_sort(arr: list[int]) -> list[int]:
    """
    Time complexity:    O(n^2)
    Space complexity:   O(1)
    Swaps:              O(n^2)
    Stable:             Yes
    """
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


if __name__ == "__main__":
    nums = [3, 5, 1, 2, 9, 4, 6, 8, 7, 0]
    print(insertion_sort(nums))