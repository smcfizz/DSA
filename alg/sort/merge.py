from typing import List


def merge_sort(nums: List) -> List:
    def merge(left, right):
        merged = []
        left_idx, right_idx = 0, 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1
        merged.extend(left[left_idx:])
        merged.extend(right[right_idx:])
        return merged

    middle = len(nums) // 2
    if len(nums) <= 1:
        return nums
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])
    return merge(left, right)


if __name__ == '__main__':
    nums = [3, 5, 1, 2, 9, 4, 6, 8, 7, 0]
    print(merge_sort(nums))