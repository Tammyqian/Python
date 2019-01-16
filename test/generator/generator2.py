# -*- coding:utf-8 -*-

def flatten(nested):
    try:
        #不要迭代类似字符串的对象
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested
print list(flatten(['foo',5,['bar',['baz']]]))

def flatten2(nested):
    result = []
    try:
        #不要迭代类似字符串的对象
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten2(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result
print list(flatten2(['foo',5,['bar',['baz']]]))