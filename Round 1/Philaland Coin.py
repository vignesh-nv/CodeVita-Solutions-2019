
t = int(input())

for i in range(t):
    n = int(input())
    ans = 0
    while n:
        ans+=1
        n //=2
    print(ans)
