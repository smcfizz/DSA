import math


def radix_sort(arr: list[int]) -> list[int]:
    """
    Time complexity:    O(n * k) average, where n is len of arr and k is num buckets
    Space complexity:   O(n + k)
    Moves:              O(n log n)
    Stable:             Yes
    """
    buckets = [[] for i in range(len(arr))]
    max_digits = math.floor(math.log(max(arr), 10)) + 1

    nums = arr.copy()
    for i in range(1, max_digits + 1):
        for num in nums:
            bucket = (num % 10 ** i) // 10 ** (i - 1) # isolate the value at the digit we are sorting on
            buckets[bucket].append(num)
            nums = []

        for b in reversed(buckets):
            while len(b) > 0:
                nums.insert(0, b.pop())

    return nums


if __name__ == "__main__":
    nums = [3, 5, 1, 2, 9, 4, 6, 8, 7, 0]
    print(radix_sort(nums))
    nums = [131, 59, 102, 27, 93, 415, 56, 98, 27, 7]
    print(radix_sort(nums))