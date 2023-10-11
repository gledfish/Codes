from collections import deque

que:deque[int] = deque()

que.append(1)
que.append(2)
que.append(3)
print(len(que))
pop = que.popleft()
print(pop)
print(len(que))