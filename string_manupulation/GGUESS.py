import random
import sys
n = int(input())

y = random.randint(1, n)
status = True
while status:
    print(y)
    x = str(input())
    if x == 'E':
        break
    if x == 'L':
        y = random.randint(1, y)
        print(y)
        sys.stdout.flush()
    if x == 'G':
        y = random.randint(y, n)
        print(y)
        sys.stdout.flush()