my_list = [5, 9, 3, 7, 2, 8, 1, 6]
def partition(data):
    left = []
    pivot = data[0]
    right = []
    for item in data[1:]:
        if item < pivot:
            left.append(item)
        else: # Handling > or =
            right.append(item)
    return left, pivot, right
def quicksort(data):
    if data == []:
        return data
    left, pivot, right = partition(data)
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort(my_list))




# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # TO-DO
    # Initiazing innitial array
    index_left = index_right = 0
    merged_arr = []

    while index_left < len(arrA) and index_right < len(arrB):
        if arrA[index_left] < arrB[index_right]:
            merged_arr.append(arrA[index_left])
            index_left += 1
        else:
            merged_arr.append(arrB[index_right])
            index_right += 1
    merged_arr += arrA[index_left:]
    merged_arr += arrB[index_right:]
    return merged_arr
            


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    elif len(arr) > 1:
        mid = len(arr)//2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left,right)


merge_sort(my_list)






















# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
