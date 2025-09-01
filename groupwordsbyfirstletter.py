a=["apple","ant","bat"]
freq={}
for i in a:
    if i[0] not in freq:
        freq[i[0]]=i

    else:
        freq[i[0]]+=", " +i

print(freq)

