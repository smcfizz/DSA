def selection_sort(arr: list[int]) -> list[int]:
    """
    Time complexity:    O(n^2)
    Space complexity:   O(1)
    Swaps:              O(n) on average
    Stable:             Yes
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    nums = [3, 5, 1, 2, 9, 4, 6, 8, 7, 0]
    print(selection_sort(nums))