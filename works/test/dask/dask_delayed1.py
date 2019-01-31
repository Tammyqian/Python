import dask

def inc(x):
    return x + 1

def double(x):
    return x + 2

def add(x, y):
    return x + y

data = [1,2,3,4,5]
output = []

for x in data:
    a = inc(x)
    b = double(x)
    c = add(a, b)
    output.append(c)


total = sum(output)
print total