import curses, random, sys, time
# import ceil from math

class Hangman:
    def __init__(self, s):
        s.addstr(0, 0, '  ┌─────┐')
        s.addstr(1, 0, '  │     │')
        s.addstr(2, 0, '  │    😄')
        s.addstr(3, 0, '  │')
        s.addstr(4, 0, '  │')
        s.addstr(5, 0, '  │')
        s.addstr(6, 0, '  │')
        s.addstr(7, 0, ' ─┸─')

    def five(self, s):
        s.addstr(2, 7, '😥')
        s.addstr(3, 8, '│')
        s.addstr(4, 8, '│')
        s.refresh()

    def four(self, s):
        s.addstr(2, 7, '😰')
        s.addstr(3, 8, '│')
        s.addstr(4, 8, '│')
        s.addstr(5, 7, '/ ')
        s.refresh()

    def three(self, s):
        s.addstr(2, 7, '😩')
        s.addstr(3, 8, '│')
        s.addstr(4, 8, '│')
        s.addstr(5, 7, '/ \\')
        s.refresh()

    def two(self, s):
        s.addstr(2, 7, '😱')
        s.addstr(3, 7, '\\│')
        s.addstr(4, 8, '│')
        s.addstr(5, 7, '/ \\')
        s.refresh()

    def one(self, s):
        s.addstr(2, 7, '💀')
        s.addstr(3, 7, '\\│/')
        s.addstr(4, 8, '│')
        s.addstr(5, 7, '/ \\')
        s.refresh()


cases = {
    '1': Hangman.five,
    '2': Hangman.four,
    '3': Hangman.three,
    '4': Hangman.two,
    '5': Hangman.one
}


def main(screen):
    # Game setup
    alphabet = tuple(chr(97 + x) for x in range(0, 26))
    words = []
    letters_used = []
    strikes = 0
    file = open('words.txt', "r")
    for line in file:
        words.append(line)
    file.close()
    target_word = words[random.randint(0, len(words) - 1)]
    length = len(target_word) - 1
    current_word = '░' * length

    # Board setup
    maxyx = screen.getmaxyx()
    y = maxyx[0]
    x = maxyx[1]
    key = -1
    position = 1
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
    highlight_text = curses.color_pair(2)
    used_text = curses.color_pair(1)
    normal_text = curses.A_NORMAL
    screen.border(0)
    curses.curs_set(0)
    alpha_container = curses.newwin(3, 55, int((y / 2) - 9), int((x / 2) - 26))
    alpha_container.box()
    other_container = curses.newwin(10, 55, int((y / 2)), int((x / 2) - 26))
    other_container.box()
    hangman_container = curses.newwin(9, 10, int((y / 2) - 20), int((x / 2) - 4))
    Hangman(hangman_container)
    word_container = curses.newwin(1, 55, int((y / 2) - 11), int((x / 2) - 26))

    def fill_letters(letter):
        nonlocal current_word
        nonlocal target_word

        for i in range(length):
            if target_word[i] == letter:
                other_container.addstr(6, 5, f'🔺 {target_word.index(letter)} {letter}')
                current_word = current_word[0: i] + letter + current_word[i + 1:]




    screen.refresh()
    alpha_container.refresh()
    other_container.refresh()
    hangman_container.refresh()
    word_container.refresh()

    while key != 'Q':
        key = screen.getkey()
        if strikes == 6:
            curses.endwin()
        if (key == 'KEY_DOWN' or key == 'KEY_LEFT'):
            if position > 1:
                position -= 2
                # other_container.addstr(7, 5, str(position))
                # other_container.refresh()
        elif (key == 'KEY_UP' or key == 'KEY_RIGHT'):
            if position < 51:
                position += 2
                # other_container.addstr(7, 5, str(position))
                # other_container.refresh()
        elif key in alphabet:
            position = (alphabet.index(key) * 2) + 1
            # other_container.addstr(5, 5, str(key))
            # other_container.addstr(7, 5, str(position))
            # other_container.refresh()
        else:
            letter = alphabet[int(position / 2)]
            # other_container.addstr(1, 5, f'💩 {}')
            if letter in target_word:
                letters_used.append(position)
                fill_letters(letter)
            elif position not in letters_used:
                letters_used.append(position)
                strikes += 1
                other_container.addstr(1, 5, f'💩 {strikes}')
                if strikes < 6: cases[str(strikes)](None, hangman_container)

        for i in range(0, 52):
            if i in letters_used:
                alpha_container.addstr(1, i + 1, f'{alphabet[int(i / 2)]}', used_text)
            elif (i == position):
                alpha_container.addstr(1, i + 1, f'{alphabet[int(i / 2)]}', highlight_text)
            elif i % 2 == 1:
                alpha_container.addstr(1, i + 1, f'{alphabet[int(i / 2)]}', normal_text)

        col_width = int(30 / length)
        for j in range(0, 30, col_width):
            if j < length * col_width:
                word_container.addstr(0, j + 14, f'{current_word[int(j / col_width)]}')


        other_container.addstr(3, 5, str(key))
        other_container.addstr(8, 5, str(target_word))

        screen.refresh()
        alpha_container.refresh()
        other_container.refresh()
        word_container.refresh()
    screen.clear()
    screen.addstr(int((y / 2)), int((x / 2) - 5), 'Goodbye! 👋')
    screen.refresh()
    time.sleep(1)


curses.wrapper(main)
