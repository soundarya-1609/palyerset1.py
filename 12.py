low1=list(map(int,input().split()))
low2=list(map(int,input().split()))
for n in range(0,low1[1]):
   low2=[low2[-1]]+low2[:-1]
print(*low2,end=" ")
