'''
NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
'''

import numpy as np

arr0 = np.array(42)  # 0-D array

arr1 = np.array([1, 2, 3, 4, 5]) # 1-D array

arr2 = np.array([[1, 2, 3],[4, 5, 6]]) # 2-D array

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # 3-D array

print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)