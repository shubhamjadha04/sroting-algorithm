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

