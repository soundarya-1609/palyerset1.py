nums=list(map(str,input()))
pss=ee=0
for i in range(0,len(nums)-1):
  q=nums[i]
  if int(q)!=0:
   for j in range(i+1,i+2):
    q=q+nums[j]
    if int(q)<27 and int(q)>0: pss=ps+1
    elif int(q)==0: pss=pss-1
    else: break
if pss!=1: ee=pss%2
print(pss+ee+1)
