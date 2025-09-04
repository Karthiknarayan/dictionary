# Invert a dictionary of lists.
# Input: {"a":[1,2], "b":[2,3]} → Output: {1:["a"], 2:["a","b"], 3:["b"]}


freq={"a":[1,2], "b":[2,3]}
freq2={}
for k,v in freq.items():
    for a in v:
        if a not in freq2:
            freq2[a]=list(k)

        else:
            freq2[a].append(k)

print(freq2)