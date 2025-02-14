from insertion import insertion_sort


def bucket_sort(arr: list[int], use_insertion_sort=True) -> list[int]:
    '''
    Time complexity:    O(n) average, since # buckets == arr size, O(n^2/k) otherwise
    Space complexity:   O(n + k)
    Swaps:              O(n log n)
    Stable:             No
    '''
    if len(arr) < 2:
        return arr
    
    max_val = 1 + max(arr)
    bucket_count = len(arr)
    buckets = [[] for i in range(bucket_count)]
    for a in arr:
        buckets[bucket_count * a // max_val].append(a)
    
    for i in range(len(buckets)):
        buckets[i] = insertion_sort(buckets[i]) if use_insertion_sort else bucket_sort(buckets[i])
    
    sorted = []
    for b in buckets:
        sorted += b

    return sorted


if __name__ == "__main__":
    nums = [3, 5, 1, 2, 9, 4, 6, 8, 7, 0]
    print(bucket_sort(nums))