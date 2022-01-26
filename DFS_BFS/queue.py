from collections import deque

# # 큐를 사용하기 위해 deque를 임포트
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

queue.reverse()

print(queue)
print(list(queue))
