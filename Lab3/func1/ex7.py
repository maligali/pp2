def has_33(nums):
    nums = [str(n) for n in nums]
    nums = ''.join(nums)
    return "33" in nums

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3])) 