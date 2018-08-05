import random
import sys
import time
import curses


try:
  bodies = [" ------\n |    |\n |    😄\n |\n |\n |\n |\n |\n---",
          " ------\n |    |\n |    😥\n |    |\n |    |\n |\n |\n |\n---",
          " ------\n |    |\n |    😰\n |    |\n |    |\n |   / \n |\n |\n---",
          " ------\n |    |\n |    😩\n |    |\n |    |\n |   / \ \n |\n |\n---",
          " ------\n |    |\n |    😫\n |   \|\n |    |\n |   / \ \n |\n |\n---",
          " ------\n |    |\n |    💀\n |   \|/\n |    |\n |   / \ \n |\n |\n---"]
  strikes = 0
  words = [None]
  file = open("words.txt", "r")
  for line in file:
    words.append(line)
  file.close()
  target_word = words[random.randint(0, len(words) - 1)]
  letters_left = len(target_word) - 1
  length = len(target_word) - 1
  current_word = "—" * length
  alphabet = [chr(65 + x) for x in range(0, 26)]

  def draw_body():
    print(bodies[strikes])


  def fill_letters(letter):
    global current_word
    global letters_left

    for i in range(length):
      if target_word[i] == letter:
        current_word = current_word[0: i] + letter + current_word[i + 1:]
        letters_left -= 1

  def print_word(word):
    output = ""
    for letter in word:
      output += letter + " "
    # print(f"\n\n👉 {output} 👈")
    print(f"\nThe word has {length} letters: {output}\n\n")

  print("\n\nWelcome to Hangman! 🕴")
  print_word(current_word)
  draw_body()
  print("Letters left:")
  print_word(alphabet)

  while strikes < 5 and letters_left > 0:
    print(target_word)
    print(alphabet)
    letter = input("\nPlease guess a letter: ")

    if letter.upper() not in alphabet:
      print(f"\n❌ {letter} is not a valid letter! Try again! \n")
    else:
      if letter in target_word:
        print("👌 Great!")
        fill_letters(letter)
      else:
        strikes += 1
        print(strikes, " / 5 strikes")

      print_word(current_word)
      draw_body()
      alphabet.remove(letter.upper())

    print("Letters left:")
    print_word(alphabet)

  if letters_left < 0:
    print("YOU WIN!!")
  else:
    print("YOU LOSE...word was " + target_word)



except KeyboardInterrupt:
  print('\n\n Goodbye! 👋\n')
  sys.exit()