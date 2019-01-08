# Fizzbuzz
# for a range of numbers return that number
# if number is divisible by 3 return 'fizz'
# if number is divisible by 5 return 'buzz'
# if number is divisible by both 3 and 5 return 'fizzbuzz'


def fizzbuzz(nums):
    for num in range(1, nums + 1):
        if num % 3 == 0 and num % 5 == 0:
            print('fizzbuzz')
        elif num % 3 == 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        else:
            print(num)


fizzbuzz(15)
