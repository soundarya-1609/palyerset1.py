ms1,ms2=map(str,input().split())
if(len(ms1)!=len(ms2)):
   print("no")
else:
   k1=[ms1.count(i) for i in ms1]
   k2=[ms2.count(i) for i in ms2]
if(k1==k2):
   print("yes")
else:
   print("no")
