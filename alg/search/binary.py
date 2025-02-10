def binary_search(sorted_arr: [int], target: int) -> bool:
    if len(sorted_arr) == 0:
        return False
    pos = len(sorted_arr) // 2
    if sorted_arr[pos] == target:
        return True
    elif sorted_arr[pos] < target:
        return binary_search(sorted_arr[pos + 1:], target)
    else:
        return binary_search(sorted_arr[:pos], target)

if __name__ == '__main__':
    sorted_arr = [1, 13, 35, 42, 57, 63, 71, 88, 95, 97]
    target = int(input('Enter target value between 1 and 100: '))
    if binary_search(sorted_arr, target):
        print('Found')
    else:
        print('Not found')