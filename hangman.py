import random
import re

def validate_word(word):
    return bool(re.match("[^a-zA-Z]+$", word))

def validate_difficulty(difficulty):
    return bool(re.match("^(easy|hard)$", difficulty))

def choose_word(difficulty):
    """
    This function will choose a random word from the two word lists, based on the difficulty chosen.

    Args:
        difficulty (str): The difficulty level, either 'easy' or 'hard'.

    Returns:
        str: A randomly picked word from the word list files.

    Raises:
        ValueError: If the entry is not 'easy' or 'hard' the user will be prompted to retype.
    """
    if difficulty == 'easy':
        with open('easy_words.txt', 'r',) as file:
            words = file.read().splitlines()
    elif difficulty == 'hard':
        with open('hard_words.txt', 'r') as file:
            words = file.read().splitlines()
    else:
        raise ValueError("Incorrect entry, please enter either 'easy' or 'hard'.")

    return random.choice(words)

def display_word(word, guessed_letters):
    """
    Generate a string that represents the display of the word with the correctly guessed letters revealed, and the unguessed letter hidden.

    Args:
        word (str): The word that needs to be guessed.
        guessed_letters (list): A list of letter that the user has guessed.

    Returns:
        str: A string representing the word with the guessed letter revealed, and the unguessed letters hidden.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    return display.strip()


def draw_hangman(attempts):
    hangman_graphics = [
        """
        +---+
            |
            |
            |
           ===
        """,
        """
        +---+
        0   |
            |
            |
           ===
        """,
        """
        +---+
        0   |
        |   |
            |
           ===
        """,
        """
        +---+
        0   |
       /|   |
            |
           ===
        """,
        """
        +---+
        0   |
       /|\  |
            |
           ===
        """,
        """
        +---+
        0   |
       /|\  |
       /    |
           ===
        """,
        """
        +---+
        0   |
       /|\  |
       / \  |
           ===
        """
    ]

    return hangman_graphics[attempts - 1] if attempts > 0 else ""

def hangman():
    print("Welcome to Hangman!")

    while True:
        player_choice = input("Enter '1' for Player vs Player mode, or '2' for Player vs Computer mode: ")

        if player_choice == '1':
            word_to_guess = input("Player 1, please enter the word to guess: ")
            if not validate_word(word_to_guess):
                print("Invalid word! Please enter only letters.")
                continue
            break
        elif player_choice == '2':
            while True:
                difficulty = input("Pick your difficulty level ('easy' or 'hard'): ")
                if validate_difficulty(difficulty):
                    word_to_guess = choose_word(difficulty)
            break
        else:
            print("Invalid choice. Please enter '1' or '2'.")
            
    guessed_letters = []
    max_attempts = 7
    attempts = 0

    while True:
        print(draw_hangman(attempts))
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts =+ 1
            print("Incorrect guess! Attempts left:", max_attempts - attempts)
        
        
        

