nums=[1,1,2,2,3,3,3,3,4,5,6]
# nums=[]
# # for i in range(5):
# #     a=int(input())
# #     nums.append(a)
# nums=input().split()
freq={}
for i in range (len(nums)):
    if nums[i] not in freq:
        freq[nums[i]]=1

    elif nums[i] in freq:
        freq[nums[i]]+=1
maxval=0
for i,v in freq.items():
    if v>maxval:
        maxval=i

print(f"The maximum appeared number is {maxval}\nits frequency is {freq[maxval]}") 