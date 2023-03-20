'''
Shape of an Array
The shape of an array is the number of elements in each dimension.

Get the Shape of an Array
NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
'''

import numpy as np

arr =  np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

'''
Reshaping arrays
Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.


Can We Reshape Into any Shape?
Yes, as long as the elements required for reshaping are equal in both shapes.
'''

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3) # this is return view of array not copy

print(newarr)

'''
You are allowed to have one "unknown" dimension.

Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.

Pass -1 as the value, and NumPy will calculate this number for you.

'''

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

'''
Flattening the arrays
Flattening array means converting a multidimensional array into a 1D array.

We can use reshape(-1) to do this.
'''

arr = np.array([[1, 2, 3], [4, 5, 6]])

# below both function can flatten array
newarr = arr.reshape(-1)
newarr = arr.ravel()

print(newarr)