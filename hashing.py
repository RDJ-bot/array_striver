n = 5
arr = [1,3,2,1,3]
num = 1

hash = [0]*13
for i in range(n):
    hash[arr[i]] += 1

print(hash[num])