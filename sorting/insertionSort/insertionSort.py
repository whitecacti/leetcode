# try 1
def insertionSort(arr):
    for i in range(1,len(arr),1):
        left = arr[i-1]
        right = arr[i]
        if left > right:
            arr[i] = left
            arr[i-1] = right

            count = 0
            curr = i
            while curr != 0:
                left_left = arr[i-1-count]
                left = arr[i-count]
                if left_left > left:
                    arr[i-1-count] = left
                    arr[i-count] = left_left
                curr-=1
                count+=1
    return arr

print(insertionSort([1,3,2,5,3,12,8,9,11,10,2]))

# try 2
def insertionSort(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        pointer = i - 1
    
        while pointer >= 0 and arr[pointer] > current:
            arr[pointer + 1] = arr[pointer]
            pointer -= 1

        arr[pointer + 1] = current

    return arr

print(insertionSort([1,3,2,5,3,12,8,9,11,10,2]))