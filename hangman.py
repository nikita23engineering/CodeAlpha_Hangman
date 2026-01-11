import random

words = ["python", "java", "apple", "coding", "intern"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)

    letter = input("Guess a letter: ").lower()

    if letter in used_letters:
        print("Already guessed!")
        continue

    used_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1
        print("Wrong guess!")

if "_" not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
