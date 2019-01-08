# formats phohe numbers (555) 555-5555


def formatter(pn):
    formatted_number = ''
    for i, digit in enumerate(pn):
        if i == 0:
            formatted_number += f'({digit}'
        elif i == 2:
            formatted_number += f'{digit}) '
        elif i == 5:
            formatted_number += f'{digit}-'
        else:
            formatted_number += digit
    return formatted_number


phone_number = input('Enter unformatted 10 digit phone number')

print(formatter(phone_number))
