#!/usr/bin/python3
# -*- coding: utf-8 -*-

import string

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
    "Ñ": "--.--"
}

morse_to_alphabet = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    ".-.-": "Ä",
    "..--": "Ü",
    "...--..": "ß",
    ".--.-": "À",
    ".-..-": "È",
    "..-..": "É",
    ".-.-.-": ".",
    "--..--": ",",
    "---...": ":",
    "-.-.-.": ";",
    "..--..": "?",
    "-....-": "-",
    "..--.-": "_",
    "-.--.": "(",
    "-.--.-": ")",
    ".----.": "'",
    "-...-": "=",
    ".-.-.": "+",
    "-..-.": "/",
    ".--.-.": "@",
    "--.--": "Ñ"
}


def removeunusablecharacters(uncorrected_string):
    
    correctedstring = uncorrected_string

    unusablecharacters = "§!\"#$%&*<>[\]^`{|}~"
    #print(unusablecharacters)
    for i in unusablecharacters:
        correctedstring = correctedstring.replace(i,"")

    return correctedstring


def encode(string=""):
    morsestring = []

    string = removeunusablecharacters(string)
    string = string.upper()
    words = string.split(" ")
    for word in words:
        letters = list(word)

        morseword = []
        for letter in letters:
            morseletter = alphabet_to_morse[letter]
            morseword.append(morseletter)

        word = "/".join(morseword)
        morsestring.append(word)

    return "//".join(morsestring)


def decode(string=""):
    characterstring = []

    words = string.split("//")
    for word in words:
        letters = word.split("/")

        characterword = []
        for letter in letters:
            characterletter = morse_to_alphabet[letter]
            characterword.append(characterletter)

        word = "".join(characterword)
        characterstring.append(word)

    return " ".join(characterstring)

def _check(string=""):

    teststring = removeunusablecharacters(string)
    encodestring = encode(string)
    decodestring = decode(encodestring)

    print(string)
    print(teststring)
    print(encodestring)
    print(decodestring)

    if teststring.upper() == decodestring:
        return True
    else:
        return False

