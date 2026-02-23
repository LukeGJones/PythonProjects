num = int(input("Enter a number: "))
nums = []
firstSkipped = True

for i in range(1,num+1):
    nums.append(i)

step = 2
for i in range(step - 1,len(nums)):
    firstSkipped = True
    for j in range(step - 1,len(nums),step):
        if(firstSkipped == False):
            nums[j] = ""
        firstSkipped = False
    for i in range(step,len(nums)):
        if nums[i] != "":
            step = nums[i]
            break
nums = [x for x in nums if x != ""]
print(nums)