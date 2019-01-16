nested = [[1,2],[3,4],[5]]

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

ge = flatten(nested)
print ge
for num in ge:
    print num


def flatten2(nested):
    try:
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield nested
print list(flatten2([[[1],2],3,4,[5,[6,7]],8]))
