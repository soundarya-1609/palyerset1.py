as2,bs2=map(int,input().split())
ls=list(map(int,input().split()))
l2=[]
for i in range(0,bs2):
     u2,v2=map(int,input().split())
     l2.append([u2,v2])
for i in range(bs2):
     lower=l2[i][0]
     upper=l2[i][1]
 as2=sum(ls[lower-1:upper])
     print(as)
