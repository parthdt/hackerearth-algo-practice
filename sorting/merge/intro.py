def merge_sort(arr):
    # The last array split
    lCount, rCount = 0, 0
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left,lCount = merge_sort(arr[:mid])
    right,rCount = merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy(),lCount+rCount)


def merge(left, right, merged,count):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            count+=1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged, count

n = int(input())
array, count = merge_sort(list(map(int,input().split())))
print(count)
