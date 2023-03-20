'''
A dimension in arrays is one level of array depth (nested arrays).

nested array: are arrays that have arrays as their elements.

'''

'''
------------------------------------------------------------------
0-D Arrays
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
------------------------------------------------------------------
1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

These are the most common and basic arrays.
------------------------------------------------------------------
2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.
------------------------------------------------------------------

3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.
------------------------------------------------------------------
'''

import numpy as np

arr0 = np.array(42)  # 0-D array

arr1 = np.array([1, 2, 3, 4, 5]) # 1-D array

arr2 = np.array([[1, 2, 3],[4, 5, 6]]) # 2-D array

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # 3-D array

print(arr0)
print(arr1)
print(arr2)
print(arr3)