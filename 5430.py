from collections import deque
import sys

n = int(sys.stdin.readline())
err = False
for _ in range(n):
    command = sys.stdin.readline()
    length= int(sys.stdin.readline())
    data = sys.stdin.readline()[1:-2].split(',')

    if data[0] != '':
        data = deque(data)
    else:
        data = deque()
    direction = True

    for com in command:
        if com == 'R':
            if direction == True:
                direction = False
            elif direction == False:
                direction = True
        elif com == 'D':
            if len(data) == 0:
                print('error')
                err = True
                break
            if direction == True:
                data.popleft()
            elif direction == False:
                data.pop()

    if command.count('R') % 2 != 0:
        data.reverse()
    if err == False:
        print("[",end="")
        for i in range(len(data)):
            print(data[i],end="")
            if i != len(data)-1:
                print(",",end="")
        print("]")
    err = False