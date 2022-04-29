import sys


arg = [arg for arg in sys.argv][1:]


if __name__ == "__main__":
    if len(arg) == 1:
        num = int(arg[0])
        if num > 1:
            for i in range(2, num // 2):
                if (num % i) == 0:
                    print(f'{num} is not a prime number')
                    break
            else:
                print(f'{num} is a prime number')
        else:
            print(f'{num} is not a prime number')
    else:
        print(f'This script only excepts 1 arguement, {len(arg)} were given.')
