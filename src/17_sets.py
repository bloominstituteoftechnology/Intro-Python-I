import random
nums = set()

while len(nums) < 10:
    n = random.randint(1, 100)
    nums.add(n)


def hasFifty(nums):
    isFifty = False
    for num in nums:
        if num == 50:
            isFifty = True
    if isFifty:
        print("Set contains number 50")
    else:
        print("Set does not contain number 50")


print(nums)
hasFifty(nums)
print(len(nums))
