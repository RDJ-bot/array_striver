'''
#optimal
arr = [1,2,3,4,5,6,7]
d = 3
d = d%len(arr)

arr = arr[d:]+arr[:d]
print(arr)
'''

#brute
arr = [1,2,3,4,5,6,7]
d = 10
d = d%len(arr)
for i in range(d):
    temp = arr[0]
    for j in range(1,len(arr)):
        arr[j-1] = arr[j]
    arr[len(arr)-1] = temp
print(arr) 