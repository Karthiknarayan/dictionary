l="moon is deer"

i=0
j=1
freq={}
while i<len(l) and j<len(l):
    if l[i]==l[j]:
        if l[i] not in freq:
            freq[l[i]]=2
        
        else:
            freq[l[i]]+=1

    i+=1
    j+=1

print(freq)

        