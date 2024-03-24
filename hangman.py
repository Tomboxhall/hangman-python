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
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    return display.strip()



