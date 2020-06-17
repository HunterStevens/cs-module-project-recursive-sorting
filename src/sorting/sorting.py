# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    cur_a = cur_b = cur_merged = 0
    while cur_merged < len(merged_arr):
        if cur_a == len(arrA):
            merged_arr[cur_merged] = arrB[cur_b]
            cur_merged += 1
            cur_b += 1
        elif cur_b == len(arrB):
            merged_arr[cur_merged] = arrA[cur_a]
            cur_merged += 1
            cur_a += 1         
        elif arrA[cur_a] > arrB[cur_b]:
            merged_arr[cur_merged] = arrB[cur_b]
            cur_merged += 1
            cur_b += 1
        else:
            merged_arr[cur_merged] = arrA[cur_a]
            cur_merged += 1
            cur_a += 1              
    return merged_arr

print(merge([7,8,9],[1,2,3]))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr, level=1):
    print(f"\n merge_sort called {arr} at level {level}")
    # Your code here
    if len(arr) <= 1:
        return arr
    split_index = len(arr)//2
    left = arr[ :split_index]
    right = arr[split_index: ]
    print(f"split made {left} + {right} at level {level}")
    
    arrB = merge(merge_sort(left, level=level+1), merge_sort(right, level=level+1))
    print(f"merge happened {arrB} at level {level} \n")
    return arrB

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
