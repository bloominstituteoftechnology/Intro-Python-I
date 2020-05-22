import msvcrt

while True:
    character = msvcrt.getch()
    print(repr(character))
    print((ord(character)))

    if character == b'q':
        break
