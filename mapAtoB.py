ids=[101,102,101]
names=["A","B","C"]
freq={}
i=0
j=0
#two pointer approach
while i<len(ids) and j<len(names):
    if ids[i] not in freq:
        freq[ids[i]]=names[j]

    else:
        freq[ids[i]]+=", "+names[j]

    i+=1
    j+=1    

print(freq)