import dask.array as da
import numpy as np
# 1.example----- HelloWorld
x = np.arange(1000)
print x
y = da.from_array(x, chunks=(100))
print y
print y.mean()
print y.mean().compute()

print '--------------------------'

# 2.example
x = da.random.normal(0, 1, size=(100,100), chunks=(10, 10))
a = x.mean().compute()
print a
print '------------------------'

# 3.
import dask.bag as db
b = db.from_sequence([1, 2, 3, 4, 5, 6])
print b
c = db.from_sequence([1, 2, 3, 4, 5, 6], npartitions=2)
print c

