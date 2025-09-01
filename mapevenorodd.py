l=[1,2,3,4,5]

freq={}

for i in range(len(l)):
    freq[l[i]]="odd" if l[i]%2!=0 else "even"

print(freq)