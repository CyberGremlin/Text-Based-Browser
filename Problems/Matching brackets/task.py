import sys
from re import search
from collections import deque


def error_status():
    print('ERROR')
    sys.exit()


text = deque(_ for _ in input() if search(r'[()]', _))
if (len(text) % 2 != 0) or text[0] != '(':
    error_status()
while text:
    if text.popleft() == text.pop():
        error_status()
print('OK')
