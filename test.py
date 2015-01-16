import unittest
import morse
import inspect
import re

class TestTranslationMaps(unittest.TestCase):

    def test_alphabet_intersect(self):
        # make sure we have the info to translate back and forth
        alphabet_keys = morse.alphabet_to_morse.keys()
        alphabet_values = morse.morse_to_alphabet.values()
        for k in alphabet_keys:
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

    def test_dup_keys(self):
        def test_dict(name):
            code = inspect.getsource(morse)
            dict_code = re.findall(name + " = {.*?}", code, re.MULTILINE|re.DOTALL)[0]
            keys = re.findall("\"(.*?)\":", dict_code)
            viewed = set()
            for k in keys:
                self.assertNotIn(k, viewed)
                viewed.add(k)
        test_dict("alphabet_to_morse")
        test_dict("morse_to_alphabet")

if __name__ == '__main__':
    unittest.main()
