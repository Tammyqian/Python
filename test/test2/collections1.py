from collections import deque
q = deque(range(5))
print q,type(q)
q.append(5)
print q
q.appendleft(6)
print q
print '-----------------'
print q.pop()
print q
print q.popleft()
print q
print q.rotate(3)
print q
q.rotate(-1)
print q