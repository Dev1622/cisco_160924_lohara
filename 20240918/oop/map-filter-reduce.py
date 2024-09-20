nums = [2,3,4]
#map syntax
#map(<func>,iterable)

nums_square = list(map(lambda num : num**2,nums))
print(nums_square)



nums_even = list(filter(lambda n : n % 2 == 0,nums))
print(nums_even)


from functools import reduce
nums = [10,20,30]
nums_sum = reduce((lambda sum, num : sum+num), nums,0)
nums_prod = reduce((lambda p,num : p * num),nums,1)

import sys
nums_min = reduce(lambda m,num: min(m,num),nums,sys.maxsize)
nums_max = reduce(lambda m,num : max(m,num),nums,-sys.maxsize)

#nums_min = reduce(min,nums)    also can use this
#nums_max = reduce(max,nums)    also can use this

print(nums_sum)
print(nums_prod)
print(nums_min)
print(nums_max)

