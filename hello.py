import numpy as np

x = np.array([1,2,3])
print(x)
print(type(x))

x = np.array((1,2,3))
print(x)
print(type(x))

x = np.array(1,2,3) # WRONG
print(x)

x = list(range(10))
print(x)
print(type(x))

x = np.arange(10)
print(x)
print(type(x))
