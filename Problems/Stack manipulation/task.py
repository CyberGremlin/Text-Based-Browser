from collections import deque

n = int(input())
my_stack = deque()

for i in range(n):
    query = input()

    if 'POP' in query:
        my_stack.popleft()
    else:
        my_stack.appendleft(query.split()[-1])

for _ in my_stack:
    print(_)
