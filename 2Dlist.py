# First method to create 1D array
N = 5
arr = [0]*N
print(arr)

# Second method to create 1D array
N = 5
arr = [0 for i in range(N)]
print(arr)

# First method to create 2D array
rows, cols = (5,5)
arr = [[0]*cols]*rows
print(arr)

# Second method to create 2D array
rows, cols = (5,5)
arr = [[0 for i in range(cols)] for j in range(rows)]
print(arr)

# Method 2b
rows, cols = (5,5)
arr = []
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    arr.append(col)

print(arr)
