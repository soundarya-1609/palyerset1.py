xs,ys=input().split()
ds=abs(len(ys)-len(xs))
for i in range(len(xs)):
    if(len(ys)==1 and y[i] in xs):
        break
    if (xs[i]!=ys[i]):
        d=d+1
print(d)
