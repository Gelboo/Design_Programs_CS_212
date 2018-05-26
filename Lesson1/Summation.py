# create function to summation the square numbers of an list

def ss(nums):
    '''take list as input and return
    the summation of the square list items x^2'''
    total = 0
    for i in range(len(nums)):
        total += nums[i]**2
    return total

l = [1,2,3,4]
print(ss(l))

## another solution might be
def ss2(nums):
    return sum(x**2 for x in nums)
