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
        
    ]


