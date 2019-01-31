strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')

counts = {}

for kw in strings:
    if kw not in counts:
        counts[kw] = 1
    else:
        counts[kw] +=1
print counts

counts1 = dict()
for kw in strings:
    counts1[kw] = counts1.setdefault(kw,0) + 1
print counts1


from collections import defaultdict
n = defaultdict()
d = defaultdict(dict)
l = defaultdict(list)
print n,d,l
d['a']=1
l['a']=1
print d,l
print d,l['b'],d['b']
print d,l['c'].append('c')
print d,l