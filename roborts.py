dir=list(input())
lenth=len(dir)
res=[0]*lenth
times=10e99
for i in range(lenth):
    index=i
    tmp=[]
    while True:
        if dir[index]=='R':
            index+=1
        else:
            index-=1
        if index in tmp:
            break
        else:
            tmp.append(index)
    inx=tmp[int(times%len(tmp))-1]
    res[inx]+=1
res=list(map(str,res))
res=' '.join(res)
print(res)

#RRLRL 0 1 2 1 1