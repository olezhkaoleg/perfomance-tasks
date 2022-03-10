adrs = input('file with numbers address ')

nums = []

with open(adrs) as f:
  for line in f:
    nums.append(int(line))
    
def min_prog(list):
  return sum(abs(sorted(nums)[round(len(nums) / 2)] - i) for i in nums)

print(min_prog(nums))
