# sorting algorithm 

# bubble sort 
def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    print(lst)


# selection sort
def selection_sort(lst):
    for i in range(len(lst)):

        min_index = i

        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j


        lst[i], lst[min_index] = lst[min_index], lst[i]

    print(lst)



# Insertion Sort
def inse(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    print(arr)


# merge sort 
def merge(left,right):
  res = []
  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      res.append(left[i])
      i+=1
    else:
      res.append(right[j])
      j+=1

  if i < len(left):
    while i < len(left):
      res.append(left[i])
      i+=1
      
  if j< len(right):
    while j <len(right):
      res.append(right[j])
      j+=1

  return res

def merge_sort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr)//2

  left = arr[:mid]
  right = arr[mid:]

  left = merge_sort(left)
  right = merge_sort(right)

  return merge(left,right)







