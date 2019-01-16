mySet = []
for i in range(10):
    mySet.append(set(range(i,i+5)))

print reduce(set.union,mySet)