import random

def get_names():
    names = []
    for i in range(1,5):
        while True:
            name = input(f"Enter your name{i}: ")
            if name.isdigit():
                print(f"name{i} can not be a number. try again.")
            else:
                names.append(name)
                break
    return names
names = get_names()
print(names)

guess_word = random.choice(names)
z = len(guess_word)

hidden_word = ['_' for _ in range(z)]
# print(hidden_word)

print(f"the chosen word has {z} letters:{' ' .join(hidden_word)}")

attempts = z
guessed_letters = []

while attempts > 0:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("please enter a valid single letter.")
        continue

    if guess in guessed_letters:
        print(f"you alredy guessed the letter '{guess}' try another one.")
        continue

    guessed_letters.append(guess)

    if guess in guess_word:
        print(f"Good guess! the letter '{guess}' is in the word.")

        for index, letter in enumerate(guess_word):
            if letter == guess:
                hidden_word[index] = guess

        print("current word:", ' '.join(hidden_word))

        if '_' not in hidden_word:
            print(f"congratuletions! you guessed the word '{guess_word}'")
            break

    else:
        attempts -= 1
        print(f"wrong guess! you have '{attempts}' attempts left")

    if attempts == 0:
        print(f"sorry, you've run out of guesses. the word was '{guess_word}'")

