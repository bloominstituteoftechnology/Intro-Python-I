# formats phohe numbers (555) 555-5555


def formatter(pn):
    formatted_number = ''
    if len(pn) != 10:
        new_number = input(
            f'You gave me {len(pn)} digits. Please enter 10 digits: ')
        return formatter(new_number)
    verified = input(f'Your number is {pn}. Is this correct [y/n]? ')
    if verified.lower() == 'y' or verified.lower() == 'yes':
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
    elif verified.lower() == 'n' or verified.lower() == 'no':
        updated_number = input(f'Try not to be so clumsy this time: ')
        return formatter(updated_number)
    else:
        return "I don't know what you mean. See ya!"


phone_number = input('Enter unformatted 10 digit phone number: ')

print(formatter(phone_number))
