l=[1,1,2,3,4,5,5,6]
j=0
n=len(l)
for i in range(n-1):
    if l[i+1]!=l[i]:
        l[j]=l[i]
        j+=1 
l[j]=l[n-1]
j+=1 
for i in range(j):
    print(l[i],end=" ")