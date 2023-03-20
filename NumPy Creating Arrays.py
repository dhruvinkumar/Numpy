'''
NumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function.
'''

import numpy as np

a = np.array([1, 2, 3, 4, 5])  # Creating array from list

b = np.array((10, 20, 30, 40, 50))  # Creating array from tuple

print(a)
print(b)

print(type(a))
print(type(b))
'''
To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray
'''