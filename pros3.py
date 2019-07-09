sound,vi=input().split()
AS=abs(len(sound)-len(vi))
for i in range(len(sound)):
  if len(vi)==1 and vi[i] in sound:
   break
  if sound[i]!=vi[i]:
   AS+=1
print(AS)
© 2019 GitHu
