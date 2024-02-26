def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  p = arr[len(arr) // 2]
  list_left = [i for i in arr if i < p]
  list_right = [i for i in arr if i > p]
  return quick_sort(list_left) + [p] + quick_sort(list_right)