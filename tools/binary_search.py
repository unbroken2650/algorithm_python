def binary_search(arr, t, low, high):
    if low >= high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == t:
        return mid
    elif arr[mid] > t:
        high = mid - 1
    else:
        low = mid + 1
    return binary_search(arr, t, low, high)
