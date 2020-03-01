"""
Tutorial - https://numpy.org/devdocs/user/quickstart.html#
Data types - https://numpy.org/devdocs/user/basics.types.html
"""
import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.single)     # The type of the resulting array is deduced from the type of the elements in the sequences.

print('Array = {}, \narray data type = {}\n'.format(array, type(array)))
print('Associated data type = {}, axes (dimensions) = {}, shape = {}, size = {}, timesize = {}'.format(array.dtype,    # an object describing the type of the elements in the array
                                                                                        array.ndim,         # the number of axes (dimensions) of the array
                                                                                        array.shape,        # for a matrix with n rows and m columns, shape will be (n,m)
                                                                                        array.size,         # the total number of elements of the array
                                                                                        array.itemsize))    # the size in bytes of each element of the array
