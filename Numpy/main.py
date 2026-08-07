# data = [1, 2, 3, 4]
# result = []

# for x in data:
#     result.append(x * 2)

# print(result) 

import numpy as np
# a = np.array([1,3,4])
# print(a)
# print(type(a))


data = np.array([1, 2, 3, 4])
result = data * 2
print(result) 

a = np.array([10, 20, 30])
b = np.zeros(5)
c = np.ones(3)
d = np.arange(1, 6) 

print(a)
print(b)
print(c)
print(d) 

a = np.array([1, 2, 3])

print(a + 10)
print(a * 2)
print(a > 1) 

# These are frequently used in data analysis.
a.sum()
a.mean()
a.max()
a.min()

matrix = np.array([[1, 2], [3, 4]])
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])