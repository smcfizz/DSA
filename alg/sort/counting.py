from collections import defaultdict


def counting_sort(nums: list[int]) -> list[int]:
    """
    Time complexity:    O(n + k) average
    Space complexity:   O(n + k)
    Moves:              O(n)
    Stable:             Yes
    """
    count = defaultdict(int)
    res = [0] * len(nums)

    for n in nums:
        count[n] += 1

    for i in range(1, len(nums) + 1):
        count[i] += count[i - 1]
    
    for n in reversed(nums):
        count[n] -= 1
        res[count[n]] = n

    return res


if __name__ == '__main__':
    nums = [3, 5, 1, 2, 9, 4, 6, 8, 7, 0]
    print(counting_sort(nums))