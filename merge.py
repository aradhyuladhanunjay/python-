import numpy as np
n=int(input())
m=n
entries = list(map(int, input().split()))
matrix = np.array(entries).reshape(n, m)
print(matrix)