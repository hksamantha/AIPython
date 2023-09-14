
def count_pairs(nums, target):
    result=0
    for nums[i] + nums[j]<target:
    result+=1
    return result

print(count_pairs(list(int(input("Enter your numbers: "))), int(input("Enter your targer value: "))))
    
