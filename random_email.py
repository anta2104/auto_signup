import random


def randomWord(length):
    consonants="bcdfghjklmnpqrstvwxyz"
    vowels="aeiou"

    return "".join(random.choice((consonants,vowels)[i%2]) for i in range(length))

