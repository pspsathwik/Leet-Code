import random
import statistics
start = int(input())
end = int(input())
n = int(input())
l1 = []
for i in range(0,n):
    l1.append(random.randint(start,end))
print(l1)
m = statistics.mean(l1)
print(round(m,2))
