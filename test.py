import unittest
import morse

class TestTranslationMaps(unittest.TestCase):

    def test_alphabet_intersect(self):
        # make sure we have the info to translate back and forth
        alphabet_keys = morse.alphabet_to_morse.keys()
        alphabet_values = morse.morse_to_alphabet.values()
        print set(alphabet_keys)- set(alphabet_values)
        for k in alphabet_keys:
            print k
            self.assertIn(k, alphabet_values)

    def test_morse_intersect(self):
        # make sure we have the info to translate back and forth
        morse_keys = morse.morse_to_alphabet.keys()
        morse_values = morse.alphabet_to_morse.values()
        for k in morse_keys:
            self.assertIn(k, morse_values)
    
    def test_convert_twice(self):
        alphabet_keys = morse.alphabet_to_morse.keys()
        for k in alphabet_keys:
            m = morse.alphabet_to_morse[k]
            k2 = morse.morse_to_alphabet[m]
            self.assertEqual(k, k2)

if __name__ == '__main__':
    unittest.main()
