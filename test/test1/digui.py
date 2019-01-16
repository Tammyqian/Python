def jiechen(n):
    if n == 1:
        return 1
    else:
        return n * jiechen(n-1)

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

def search(sequench, number, lower=0, upper=None):

    if upper is None:
        upper = len(sequench) - 1
    if lower == upper:
        assert number == sequench[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequench[middle]:
            return search(sequench, number, middle+1, upper)
        else:
            return search(sequench, number, lower, middle)

if __name__ == '__main__':
    # n = input('Please input n: ')
    n = 5
    print jiechen(n)
    print power(3, n)
    seq = [34,67,8,123,4,100,95]
    seq.sort()
    print seq
    print search(seq,34)
