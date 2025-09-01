a="this is an apple"

i=0
j=0
freq={}
for j in range(len(a)-1):
    if a[j]==" " or j==len(a)-1:
        if a[i:j] not in freq:
            freq[a[i:j]]=1
        else:
            freq[i:j]+=1
        i=j

print(freq)
