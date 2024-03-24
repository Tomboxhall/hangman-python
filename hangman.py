import random
import re

def validate_word(word):
    return bool(re.match("[^a-zA-Z]+$", word))

