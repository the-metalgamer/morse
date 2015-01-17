import unittest
import morse
import inspect
import re

class TestTranslationMaps(unittest.TestCase):
    
    def test_convert_twice(self):
        """We should be able to convert all charaters to morse and back"""
        alphabet_keys = morse.alphabet_to_morse.keys()
        for k in alphabet_keys:
            m = morse.alphabet_to_morse[k]
            self.assertEqual(k, morse.morse_to_alphabet[m])

    def test_dup_keys(self):
        """Both mappings should have the same amount of keys or there is probably a duplicate key"""
        self.assertEqual( len(morse.alphabet_to_morse), len(morse.morse_to_alphabet))

    def test_encode(self):
        phrase = "The quick red fox jumped over the lazy dog 1234567890"
        encoded = morse.encode(phrase)
        decoded = morse.decode(encoded)
        self.assertEqual(phrase.lower(), decoded.lower())

if __name__ == '__main__':
    unittest.main()
