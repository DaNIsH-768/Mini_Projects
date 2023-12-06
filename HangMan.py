import random

words = [
    "elephant",
    "tiger",
    "giraffe",
    "penguin",
    "zebra",
    "kangaroo",
    "dolphin",
    "cheetah",
    "octopus",
    "rhinoceros",
    "hippopotamus",
    "koala",
    "alligator",
    "crocodile",
    "panda",
    "orangutan",
    "lemur",
    "squirrel",
    "flamingo",
    "ostrich",
    "jaguar",
    "parrot",
    "armadillo",
    "platypus",
    "gazelle",
    "hedgehog",
    "iguana",
    "jellyfish",
    "kookaburra",
    "lemming",
    "mongoose",
    "narwhal",
    "ocelot",
    "pangolin",
    "quokka",
    "raccoon",
    "salamander",
    "tapir",
    "urial",
    "vulture",
    "wallaby",
    "x-ray tetra",
    "yak",
    "zebu",
    "axolotl",
    "bison",
    "chameleon",
    "dingo",
    "echidna",
    "falcon",
    "gibbon",
    "hyena",
    "ibex",
    "jackal",
    "kangaroo rat",
    "lemur",
    "meerkat",
    "numbat",
    "otter",
    "puma",
    "quail",
    "rattlesnake",
    "starfish",
    "toucan",
    "urutu",
    "viper",
    "wombat",
    "xenopus",
    "yabby",
    "zeedonk"
]


images = [
  """
   +---+
   |   |
       |
       |
       |
       |
  ========
  """,
  """
   +---+
   |   |
   O   |
       |
       |
       |
  ========
  """,
  """
   +---+
   |   |
   O   |
   |   |
       |
       |
  ========
  """,
  """
   +---+
   |   |
   O   |
  /|   |
       |
       |
  ========
  """,
  """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
  ========
  """,
  """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
  ========
  """,
  """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
  ========
  """
]


total_words = len(words)


def word_generator():
    index = random.randint(0, total_words)
    return words[index]


def blank_generator(word):
    blanks = []
    for char in word:
        blanks.append('_')
    return blanks


word = word_generator()
blanks = blank_generator(word)

wrong_guesses = 0
guesses = []

while True:
    print(images[wrong_guesses])
    for blank in blanks:
        print(blank, end=" ")

    print(f"\nYour guesses: {guesses}")
    print(f"Guesses left: {6-wrong_guesses}")
    guess = input("\nEnter your guess: ")

    if guess in word and guess not in guesses:
        for i in range(len(word)):
            if guess == word[i]:
                blanks[i] = guess
    else:
        wrong_guesses += 1

    guesses.append(guess)
    if wrong_guesses == 6:
        print(images[wrong_guesses])
        print(f"The correct answer was: {word}")
        print("Better Luck Next Time...")
        break
    if "_" not in blanks:
        print("\nYou Did it!!!")
        break

