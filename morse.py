#!/usr/bin/python3
# -*- coding: utf-8 -*-

alphabet_to_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "Ä": ".-.-",
    "Ü": "..--",
    "ß": "...--..",
    "À": ".--.-",
    "È": ".-..-",
    "É": "..-..",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    ";": "-.-.-.",
    "?": "..--..",
    "-": "-....-",
    "_": "..--.-",
    "(": "-.--.",
    ")": "-.--.-",
    "'": ".----.",
    "=": "-...-",
    "+": ".-.-.",
    "/": "-..-.",
    "@": ".--.-.",
    "Ñ": "--.--",
    " ": " ",
    "" : ""
}

morse_to_alphabet = {v: k for k, v in alphabet_to_morse.iteritems()}


def removeunusablecharacters(uncorrected_string):
    return filter(lambda char: char in alphabet_to_morse, uncorrected_string.upper())


def encode(decoded):
    morsestring = []

    decoded = removeunusablecharacters(decoded)
    decoded = decoded.upper()
    words = decoded.split(" ")
    for word in words:
        letters = list(word)

        morseword = []
        for letter in letters:
            morseletter = alphabet_to_morse[letter]
            morseword.append(morseletter)

        word = "/".join(morseword)
        morsestring.append(word)

    return " ".join(morsestring)


def decode(encoded):
    characterstring = []

    words = encoded.split(" ")
    for word in words:
        letters = word.split("/")

        characterword = []
        for letter in letters:
            characterletter = morse_to_alphabet[letter]
            characterword.append(characterletter)

        word = "".join(characterword)
        characterstring.append(word)

    return " ".join(characterstring)
