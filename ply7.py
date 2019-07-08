devi=list(input())
for i in range(0,len(devi),2):
   devi[i],devi[i+1]=devi[i+1],devi[i]
pri=''.join(devi)
print(pri)
