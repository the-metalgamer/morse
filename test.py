import unittest
import morse
import random

class TestTranslationMaps(unittest.TestCase):
    '''Test the validity of the morse module'''
    def test_convert_twice(self):
        """We should be able to convert all charaters to morse and back"""
        alphabet_keys = morse.alphabet_to_morse.keys()
        for k in alphabet_keys:
            morse_code = morse.alphabet_to_morse[k]
            self.assertEqual(k, morse.morse_to_alphabet[morse_code])

    def test_dup_keys(self):
        """Both mappings should have the same amount of keys or there is probably a duplicate key"""
        self.assertEqual(len(morse.alphabet_to_morse), len(morse.morse_to_alphabet))

    def test_encode(self):
        '''Test encoding and decoding of normal charaters'''
        phrase = "The quick red fox jumped over the lazy dog 1234567890"
        encoded = morse.encode(phrase)
        decoded = morse.decode(encoded)
        self.assertEqual(phrase.lower(), decoded.lower())

    def test_removeunusablecharacters(self):
        '''Make sure we remove unknown charaters for a translation'''
        test_str = "".join(chr(i) for i in range(256))
        corrected = morse.removeunusablecharacters(test_str)
        for char in corrected:
            self.assertIn(char, morse.alphabet_to_morse)

    def test_strencode_decode_exaustive(self):
        '''Evil test'''
        all_chr = [chr(i) for i in range(256)]
        many_chr = all_chr * 4 + list('        ') * 32
        random.shuffle(many_chr)
        phrase = "".join(many_chr)
        expected_decode = morse.removeunusablecharacters(phrase).lower()
        encoded = morse.encode(phrase)
        decoded = morse.decode(encoded)
        self.assertEqual(expected_decode, decoded.lower())


if __name__ == '__main__':
    unittest.main()
