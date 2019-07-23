ms1,ms2=map(int,input().split())
for i in range(1,100000):
   if(i%ms1==0 and i%ms2==0):
      print(i)
      break
