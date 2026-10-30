import numpy

array1 = numpy.array([[1, 2], [3, 4]])
print('Array1:\n', array1)

array2 = numpy.array([[5, 6], [7, 8]])
print('\nArray2:\n', array2)

kroneckerProduct = numpy.kron(array1, array2)
print('\nKronecker Product:\n', kroneckerProduct)