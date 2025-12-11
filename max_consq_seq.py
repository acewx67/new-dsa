nums = [1,2,3,4,100,5,6,7]
# min_num = min(nums)
hm = {}
for num in nums:
    hm[num] = 0
max_chain = 0
cur_chain = 0
for num in hm.keys():
    if num-1 in hm:
        continue
    i = 0
    temp_num = num
    while i < len(hm.keys()):
        if temp_num+1 in hm:
            cur_chain += 1
            if cur_chain > max_chain:
                max_chain = cur_chain
            temp_num += 1
        else:
            cur_chain = 0
            break
        i += 1
print(max_chain+1)