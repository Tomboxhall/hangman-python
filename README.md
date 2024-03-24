# Hangman Python Game

(screenshot of the opening few lines 'Welcome to Hangman')

# Game Purpose

Welcome to the Hangman Python game! A Python console Hangman game allows players to guess letters to uncover a hidden word. It offers player-vs-player or player-vs-computer modes.

The rules are as follows:

Hangman is a word-guessing game where one player thinks of a word and the other player tries to guess it by suggesting letters within a limited number of attempts. Each incorrect guess results in part of a stick figure being drawn, and the game ends either when the word is guessed correctly or when the full stick figure is drawn, indicating a loss.

---

# How to play

- Open the hangman.py Python file.
- Select the run option on your IDE.
- You will be prompted to choose either Player vs Player, or Player vs Computer.
- If you choose Player vs Player you will then be asked to enter the word for the other Player to guess.
- If you choose Player vs Computer, then you will be prompted to select a difficulty, 'easy' or 'hard'.
- After selecting the difficulty you will see the Hangman Graphic, and be prompted to make your first letter guess.
- Continue until you either Win, by guessing all the letters, or lose, by running out of attempts.

---

# UX Design
## User Stories
### As a player of the game

- I want to be able to visually understand the purpose and progression of the game as it unfolds.
- I want to be able to see which guesses have been successful, and which one have not, helps to keep track of guesses.
- I want to be able to see the word updating as i am correctly making guesses, along with a visual progression of the 'Hangman Hanging'.
- I want the game to be simple, enjoyable, and visually appeasing to keep player interested in playing multiple rounds.

---

## Structure

The Hangman game consists of several game functions and a main loop:

### 1. validate_word(word) function

The function `validate_word(word)` ensures that the input `word` consists of only alphabetic characters. It uses a regular expression `(re.match("^[a-zA-Z]+$", word))` to check if the entire string (`word`) matches the pattern.

- `^` asserts the start of the string.
- `[a-zA-Z]` matches any single alphabetic character (lowercase or uppercase).
- `+` specifies that the preceding pattern should occur one or more times.
- `$` asserts the end of the string.

So, the entire pattern matches if the string contains only alphabetic characters from start to end. If the input `word` matches this pattern, the function returns `True`,    
indicating that the word is valid (consists of only alphabetic characters). Otherwise, it returns `False`, indicating that the word contains non-alphabetic characters.

(Input screenshots as evidence - Code/Console appearance)

### 2. validate_difficulty(difficulty)

The `validate_difficulty(difficulty)` function ensures that the input `difficulty` is either 'easy' or 'hard'. It utilizes a regular expression `(re.match("^(easy|hard)$", difficulty))` to verify if the entire string (`difficulty`) matches one of the specified options.

- `^` asserts the start of the string.
- `(easy|hard)` defines a group with two options: 'easy' or 'hard'.
- `$` asserts the end of the string.

So, the entire pattern matches if the string contains either 'easy' or 'hard' from start to end. If the input `difficulty` matches this pattern, the function returns `True`, indicating that the difficulty level is valid. Otherwise, it returns `False`, indicating that the input difficulty is not one of the specified options.

(Input screenshots as evidence - Code/Console)

### 3. choose_word(difficulty)

The `choose_word(difficulty)` function selects a word from a word list file based on the specified difficulty level:

- For 'easy' difficulty, it reads words from 'easy_words.txt'.
- For 'hard' difficulty, it reads words from 'hard_words.txt'.
- Then, it randomly selects a word from the chosen list.

This function facilitates word selection in the Hangman game, tailoring the word's complexity to the chosen difficulty. For instance, 'easy' difficulty will offer simpler words, while 'hard' difficulty will provide more challenging ones.

(Input screenshots as evidence - Code/Console)

### 4. display_word(word, guessed_letters)

The `display_word(word, guessed_letters)` function generates a string representing the display of the word being guessed. It reveals the letters that have been correctly guessed while hiding the letters that have not yet been guessed.

How the process works:

- It takes two arguments: word (the word to be guessed) and guessed_letters (a list of letters that the player has guessed).
- It iterates through each letter in the word.
- If the letter has been guessed (e.g, it is in the guessed_letters list), it is added to the display string.
- If the letter has not been guessed, it is replaced with an underscore _.
- Finally, it returns the generated display string, where guessed letters are revealed and unguessed letters are hidden.

(Input screenshots as evidence - Code/Console)

### 5. draw_hangman(attempts)

The `draw_hangman(attempts)` function generates ASCII art representing the hangman figure, adjusting its appearance based on the number of incorrect attempts made in the game.

How the process works:

- It receives the `attempts` parameter, indicating how many incorrect guesses the player has made.
- Within the function, there's a predefined list `hangman_graphics`, storing ASCII representations of the hangman figure at different stages of completion.
- Based on the value of `attempts`, the function selects the corresponding ASCII art from `hangman_graphics`.
- If the player hasn't made any incorrect attempts (attempts = 0), an empty string is returned, indicating that no hangman figure should be displayed. Otherwise, it returns 
  the appropriate ASCII art representing the hangman figure's current state.

  (Input screenshots as evidence - Code/Console)

### 6. hangman()

The `hangman()`function initiates a game of Hangman. Here's a detailed explanation:

1. Initialization:

(Screenshot of the section of the function)

- It greets the player with a welcome message.
- It prompts the player to choose between Player vs Player mode or Player vs Computer mode.
- If the player chooses Player vs Player mode, they are asked to enter a word to guess. If they choose Player vs Computer mode, they select a difficulty level, and a word is 
  chosen randomly from a corresponding word list file.

2. Game Loop:

The main loop of the game manages the gameplay:

(Screenshot of the section of the function)

- It displays the hangman figure based on the number of incorrect attempts.
- It shows the current state of the word being guessed, with guessed letters revealed and unguessed letters hidden.
- It prompts the player to guess a letter.
- It checks if the guessed letter is correct or incorrect, updating the hangman figure and the display of the word accordingly.
- It continues until the player either guesses the word correctly or runs out of attempts.

3. End of Game:

(Screenshot of the section of the function)

- If the player runs out of attempts, a message is displayed indicating the game is over, revealing the correct word.
- If the player guesses the word correctly, a congratulatory message is shown.

4. Play Again:

- After the game ends, the player is asked if they want to play again.
- If they choose 'yes', the hangman() function is called recursively to restart the game.
- If they choose 'no', a farewell message is displayed, and the program exits.

### 7. if __name__ == "__main__"

The if `__name__ == "__main__":` construct is used in Python to ensure that certain code within a script runs only when the script is executed directly, not when it's imported as a module into another script. Specifically to this project this ensures that the `hangman()` function is executed only when the Hangman script is run directly from the command line or terminal.

(screenshots of evidence)

### 8. Extras - (imports (random/re/sys) docstrings, )

In the Hangman game, the `import random`, `import re`, and `import sys` statements are used to import Python modules, which provide additional functionality needed for the game:

1. `import random`: 
- This module is used for generating random numbers, which is crucial for selecting a word randomly from the word list files based on the chosen difficulty level (choose_word() function).

(screenshot for evidence)

2. `import re`: 
- The `re` module provides support for regular expressions in Python. It is used in the `v`alidate_word()` and `v`alidate_difficulty()` functions to check if the entered word and difficulty level, respectively, match certain patterns. Regular expressions are employed to ensure that the word contains only alphabetic characters and that the difficulty level is either 'easy' or 'hard'.

(screenshot for evidence)

3. `import sys`: 
- This module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter. In the Hangman game, it is used to exit the game `(sys.exit())` when the player chooses not to play again, terminating the program execution.

(screenshot for evidence)

Overall, these import statements allow the Hangman game to utilize functionalities provided by these Python modules to implement the game logic effectively.

### Docstrings

In the Hangman project, docstrings are used extensively to provide documentation for functions and methods. Here's how they are used:

1. Function Documentation: 
- Each function in the Hangman project is documented using a docstring. Docstrings are triple-quoted strings placed immediately after the function definition. They describe the purpose of the function, its parameters, return values, and any exceptions it may raise. For example:

(screenshot to show use of docstring)

2. Method Documentation: 
- Similarly, methods within classes are documented using docstrings to explain their functionality, parameters, and return values.

(screenshot to show use of docstring)

3. Module-Level Documentation: 
- The Hangman project may also include a module-level docstring at the beginning of the script to provide an overview of the project, its purpose, and any important information for users or developers.

(screenshot to show use of docstring - docstring within a function)

---

## Technologies

- Python for the construction of the Hangman game.
- PyCharm as the IDE to develop the game within.
- GitPod as the IDE to develop the game within.
- Vs Code as the IDE to develop the game within, and bug test and fixes.
- [Github](https://github.com/) Github for hosting the source code.
- Heroku for hosting

---

## Automated Testing/Manual Testing
### Bugs/Bug Fixes
### Unfixed Bugs

---

## Accessibility Testing
### Toptal? Or Python equivalent

### Screen Reader??

---

## Deployment

---

## Credits
### Media (Image Sourcing)
### Code
### Acknowledgements

---

## Final Comments