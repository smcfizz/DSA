def heapsort(arr: list[int]) -> list[int]:
    """
    Time complexity:    O(n log n)
    Space complexity:   O(n)
    Swaps:              O(n log n)
    Stable:             No
    """
    def min_heapify(idx: int):
        size = len(arr)
        new_idx = idx
        left = idx * 2 + 1
        right = idx * 2 + 2

        if left < size and arr[left] < arr[new_idx]:
            new_idx = left
        if right < size and arr[right] < arr[new_idx]:
            new_idx = right
        if new_idx != idx:
            arr[idx], arr[new_idx] = arr[new_idx], arr[idx]
            min_heapify(new_idx)
        
    for i in range((len(arr) // 2) - 1, -1, -1):
        min_heapify(i)
    
    sorted = []
    while len(arr) > 0:
        sorted.append(arr.pop(0))
        min_heapify(0)

    return sorted


if __name__ == "__main__":
    nums = [3, 5, 1, 2, 9, 4, 6, 8, 7, 0]
    print(heapsort(nums))