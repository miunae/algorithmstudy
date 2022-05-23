import sys

def quad(x,y,n):
    global table
    global answer
    check = table[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != table[i][j]:
                answer.append('(')
                quad(x,y,n//2)
                quad(x,y+n//2,n//2)
                quad(x+n//2,y,n//2)
                quad(x+n//2,y+n//2,n//2)
                answer.append(')')
                return
    answer.append(check)
n = int(sys.stdin.readline())
table = []
answer = []
for i in range(n):
    table.append(sys.stdin.readline())
    tmp = table[i]
    table[i] = []
    for j in range(n):
        table[i].append(tmp[j])
quad(0,0,n)
print("".join(map(str,answer)))
