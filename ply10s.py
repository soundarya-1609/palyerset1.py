vvs,rr=input().split()
hh=0
for i in range(len(vvs)):
   if(vvs[i]!=rr[i]):
      hh=hh+1
if(hh==1):
  print("yes")
else:
  print("no")
      
