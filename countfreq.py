# nums=[1,1,2,3,4,5,4]
nums=[]
# for i in range(5):
#     a=int(input())
#     nums.append(a)
nums=input().split()
freq={}
for i in range (len(nums)):
    if nums[i] not in freq:
        freq[nums[i]]=1

    else:
        freq[nums[i]]+=1

print(freq.keys())
print(freq.values())
print(freq)
