from array import *

arr = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

# Accessing element in an array

print(arr[0])
print(arr[1][2])

# Updating the entire inner array
arr[1] = [16, 17, 18]

# Updating the speecific values in an inner array
arr[1][2] = 19

# Deleting the entire inner array
del arr[1]

# Accessing all the elements in an array
for i in arr:
    for j in i:
        print(j, end=' ')
    print()