import numpy as np

nums = np.arange(16, dtype='int').reshape(4, 4)
print("Original array:")
print(nums)

print("\nNew array after swapping first and last rows of the said array:")

nums = nums[[-1,1,2,0]]
print(nums)

"""
num0 = list(nums[0])
num3 = list(nums[3])
nums[0] = num3
nums[3] = num0
print(nums)
"""