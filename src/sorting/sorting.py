# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    for i in range(0, len(arrA)):
        merged_arr[i] = arrA[i]

    for i in range(0, len(arrB)):
        middle = len(merged_arr) //2
        merged_arr[middle + i] = arrB[i]

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr, level=1):
    print(f"\n merge_sort called {arr} at level {level}")
    # Your code here
    if len(arr) == 0:
        return arr
    if len(arr) > 1:
        split_index = len(arr)//2
        left = arr[ :split_index]
        right = arr[split_index: ]
        print(f"split made {left} + {right} at level {level}")
        merge_sort(left, level=level+1)
        merge_sort(right, level=level+1)
        cur_l = cur_r = 0
        while cur_l < len(left) and cur_r < len(right):
            if left[cur_l] > right[cur_r]:
                left[cur_l], right[cur_r] = right[cur_r], left[cur_l]
                cur_l += 1
            else:
                cur_r += 1        
        arr = merge(left,right)
        print(f"merge happened {arr} at level {level} \n")
    return arr

        # while cur_l < len(left) and cur_r < len(right):
        #     if left[cur_l] < right[cur_r]:
        #         arr[cur_index] = left[cur_l]
        #         cur_l += 1
        #     else:
        #         arr[cur_index] = right[cur_r]
        #         cur_r += 1
        #     cur_index += 1
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
