# -*- coding:utf-8 -*-
def fbnq(num):
    f = [0,1]
    for i in range(num):
        f.append(f[-1] + f[-2])
    return f
num = input('please input a num:')
# print fbnq(num)
fb = fbnq(num)
def fbnq2(num):
    a, b = 0, 1
    print a,'\n',b
    while b < num:
        a, b = b, a + b
        print b
fbnq2(num)
#斐波那契数列可以应用在兔子生兔子的问题上

def change(n):
    n = 'hello'
    return n
name = 'world'
print change(name),name