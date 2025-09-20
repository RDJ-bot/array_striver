def selection(arr,num):
    for i in range(len(arr)):
        if(arr[i] == num):
            return 1
    return -1

result = selection(num = 9,arr = [1,2,3,4,5,6,9])
print(result)