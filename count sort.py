#COUNT SORT
import numpy as np

n = int(input("Insert the length of the array"))

a = np.zeros(n, dtype = 'int')

print("insert the array")

for i in range(n):
    a[i] = int(input())


k = np.zeros(max(a)+1, dtype = 'int')


for i in range(n):
    k[a[i]] += 1

print(k)

#cumulative sum


for i in range(1,k.size):
    k[i] = k[i-1]+k[i]

print(k)

b = np.zeros(n, dtype='int')

for i in range(n):
    b[k[a[n-i-1]]-1]=a[n-1-i]
    k[a[n-1-i]] -=1

print("The sorted array is",b)

