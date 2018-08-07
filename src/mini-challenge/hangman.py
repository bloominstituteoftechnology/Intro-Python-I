import curses, random, sys, time

class Hangman:
    def __init__(self, s):
        s.addstr(0, 0, '  ┌─────┐')
        s.addstr(1, 0, '  │     │')
        s.addstr(2, 0, '  │')
        s.addstr(3, 0, '  │')
        s.addstr(4, 0, '  │')
        s.addstr(5, 0, '  │')
        s.addstr(6, 0, '  │')
        s.addstr(7, 0, ' ─┸─')

    def six(self, s):
        s.addstr(2, 7, '😄')
        s.refresh()

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
    '1': Hangman.six,
    '2': Hangman.five,
    '3': Hangman.four,
    '4': Hangman.three,
    '5': Hangman.two,
    '6': Hangman.one
}

def main(screen):
    maxyx = screen.getmaxyx()
    y = maxyx[0]
    x = maxyx[1]
    key = -1
    position = 1
    retry = False
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
    highlight_text = curses.color_pair(2)
    used_text = curses.color_pair(1)
    normal_text = curses.A_NORMAL
    curses.curs_set(0)
    alpha_container = curses.newwin(3, 55, int((y / 2) - 9), int((x / 2) - 26))
    instr_container = curses.newwin(10, 60, int((y / 2) - 6), int((x / 2) - 28))
    hangman_container = curses.newwin(9, 10, int((y / 2) - 20), int((x / 2) - 4))
    word_container = curses.newwin(1, 55, int((y / 2) - 11), int((x / 2) - 26))
    welcome_container = curses.newwin(1, 14, 5, int((x / 2) - 6))


    def game_logic():
        nonlocal retry
        nonlocal key
        nonlocal position
        retry = False
        winnar = False
        alphabet = tuple(chr(97 + x) for x in range(0, 26))
        strikes = 0
        letters_used = []
        words = []
        file = open('words.txt', 'r')
        for line in file:
            words.append(line)
        file.close()
        target_word = words[random.randint(0, len(words) - 1)]
        word_length = len(target_word) - 1
        current_word = '░' * word_length

        screen.border(0)
        screen.refresh()
        welcome_container.addstr(0, 0, 'H A N G M A N')
        welcome_container.refresh()
        time.sleep(0.5)
        alpha_container.box()
        Hangman(hangman_container)
        hangman_container.refresh()
        time.sleep(1)
        instr_container.addstr(1, 13, 'Use the character or arrow keys')
        instr_container.addstr(3, 17, 'Press ENTER to select')
        instr_container.addstr(5, 19, 'Press "Q" to quit')
        instr_container.refresh()

        def fill_letters(letter):
            nonlocal current_word

            for i in range(word_length):
                if target_word[i] == letter:
                    current_word = current_word[0: i] + letter + current_word[i + 1:]

        while key is not 'Q':
            key = screen.getkey()

            if key == 'KEY_DOWN' or key == 'KEY_LEFT':
                if position > 1:
                    position -= 2
            elif key == 'KEY_UP' or key == 'KEY_RIGHT':
                if position < 51:
                    position += 2
            elif key in alphabet:
                position = (alphabet.index(key) * 2) + 1
            else:
                letter = alphabet[int(position / 2)]
                if letter in target_word:
                    letters_used.append(position)
                    fill_letters(letter)

                elif position not in letters_used:
                    letters_used.append(position)
                    strikes += 1
                    cases[str(strikes)](None, hangman_container)
                    if strikes == 6:
                        break

            for i in range(0, 52):
                if i in letters_used:
                    alpha_container.addstr(1, i + 1, f'{alphabet[int(i / 2)]}', used_text)
                elif (i == position):
                    alpha_container.addstr(1, i + 1, f'{alphabet[int(i / 2)]}', highlight_text)
                elif i % 2 == 1:
                    alpha_container.addstr(1, i + 1, f'{alphabet[int(i / 2)]}', normal_text)

            col_width = int(30 / word_length)
            for j in range(0, 30, col_width):
                if j < word_length * col_width:
                    word_container.addstr(0, j + 14, f'{current_word[int(j / col_width)]}')

            winnar = current_word == target_word.strip()
            if winnar:
                instr_container.clear()
                instr_container.addstr(1, 0, '██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗')
                instr_container.addstr(2, 0, '╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║')
                instr_container.addstr(3, 0, ' ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║')
                instr_container.addstr(4, 0, '  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║')
                instr_container.addstr(5, 0, '   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║')
                instr_container.addstr(6, 0, '   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝')
                alpha_container.refresh()
                word_container.refresh()
                screen.refresh()
                instr_container.refresh()
                time.sleep(2)
                instr_container.clear()
                instr_container.addstr(1, 20, 'Press "Q" to quit')
                instr_container.addstr(3, 20, 'Press "R" to retry')
                instr_container.refresh()
                time.sleep(1)
                break

            screen.refresh()
            alpha_container.refresh()
            instr_container.refresh()
            word_container.refresh()

        while key is not 'Q':
            key = screen.getkey()
            instr_container.clear()
            instr_container.addstr(1, 19, 'Press "R" to retry')
            instr_container.refresh()
            if key is 'R':
                retry = True
                instr_container.clear()
                word_container.clear()
                alpha_container.clear()
                screen.clear()
                break

    game_logic()

    instr_container.clear()
    instr_container.refresh()
    time.sleep(1)
    while retry:
        game_logic()

    screen.clear()
    screen.addstr(int((y / 2)), int((x / 2) - 5), 'Goodbye! 👋')
    screen.refresh()
    time.sleep(1)

curses.wrapper(main)
