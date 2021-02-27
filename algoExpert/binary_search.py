def binarySearch(array, target):
    left = 0
    right = len(array)-1
    
    while left <= right:
        mid = left + right >> 1
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6]
    target = 1
    res = binarySearch(array,  target)
    print(res)