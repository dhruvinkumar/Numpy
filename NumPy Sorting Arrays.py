'''
Sorting Arrays
Sorting means putting elements in an ordered sequence.

Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.

The NumPy ndarray object has a function called sort(), that will sort a specified array.

Note: This method returns a copy of the array, leaving the original array unchanged.
'''
import numpy as np

arr = np.array([3, 2, 0, 1])

newarr = np.sort(arr)

print(arr)
print(newarr)


###########################################################

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

###########################################################

arr = np.array([True, False, True])

print(np.sort(arr))

###########################################################

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))
