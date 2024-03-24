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
    """
    Initiating the Hangman game.

    This function initiates the Hangman game, prompting the player to choose between either a Player vs Player mode
    or a Player vs Computer mode. In the Player vs Player mode, Player 1 will enter a word that needs to be
    guessed. In Player vs Computer mode, the difficulty is chosen, and a word in randomly chosen according to 
    the difficulty chosen. The game will continue until the word is either guessed correctly, or the 
    Player has run out of attempts.

    Returns:
        None
    """
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

    """
    Manage the main game loop.

    This section of code implements the main game loop, which will continuously display the hangman graphics,
    the current state of the word that is being guessed, and will prompt the Player for their guesses. It handles
    the Player inputs, it tracks the guessed letters, it will check for correct guesses, updates the attempt
    count, and will determine whether the game ends due to the Player running out of attempts or by
    successfully guessing the word correctly within the attemps allowed.

    Returns:
        None
    """
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
        
        if attempts == max_attempts:
            print("Sorry, you have ran out of attempts. The word was:", word_to_guess)
            break
        
        if all(letter in guessed_letters for letter in word_to_guess):
            print("Congratulations! You guessed the word:" word_to_guess)
            break
        
if __name__ == "__main__"
    hangman()    
        

