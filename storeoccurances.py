l="hello"
freq={}

for i in range(len(l)):
    if l[i] not in freq:
        freq[l[i]]=1

    else:
        freq[l[i]]+=1

print(freq)
    
    