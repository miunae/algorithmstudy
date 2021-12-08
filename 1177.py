import sys
def gcd(n,m):
    if n < m:
        tmp = n
        n = m
        m = tmp
    while m!=0:
        temp = n % m
        if n%m == 0:
            return m
            break
        else:
            n = m
            m = temp

n,m = map(int,sys.stdin.readline().split())
print(m-gcd(n,m))
