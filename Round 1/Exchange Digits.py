from itertools import permutations
import bisect

num1, num2 = input().split()
num2 = int(num2)
pr = []
perm = permutations(num1)

for i in list(perm):
    z = ''.join(i)
    z = int(z)
    pr.append(z)

pr = set(pr)
pr = list(pr)
pr.sort()
index = bisect.bisect(pr, num2)

if not index==len(pr):
    print(pr[index])
else:
    print(-1)
