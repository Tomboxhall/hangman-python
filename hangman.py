import random
import re

def validate_word(word):
    return bool(re.match("[^a-zA-Z]+$", word))

def validate_difficulty(difficulty):
    return bool(re.match("^(easy|hard)$", difficulty))

