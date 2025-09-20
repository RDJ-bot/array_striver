#brute force approach

'''
arr = [1,4,6,0,0,4,1,3,0,9]
temp = []
for i in range(len(arr)):
    if(arr[i] != 0):
        temp.append(arr[i])
print(temp)
for i in range(len(temp)):
    arr[i] = temp[i]
for i in range(len(temp),len(arr)):
    arr[i] = 0
print(arr)
'''

# optimal approach

arr=[1,0,2,0,3,0,4,5]
for i in range(len(arr)-1):
    if(arr[i] == 0):
        for j in range(i,len(arr)):
            if(arr[i] == 0 and arr[j] != 0):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
print(arr)