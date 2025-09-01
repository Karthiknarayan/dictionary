a=["Ram:80","Sita:90","Ram:95"]
freq={}

for i in a:
    k,v = i.split(":")

    v=int(v)
    if k in freq:
        freq[k].append(v)

    else:
        freq[k]=[v]


print(freq)