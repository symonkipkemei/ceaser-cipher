import ceaser_cipher
import unittest



class test_ceaser_cipher(unittest.TestCase):
    def test_word_reserve_if_it_keeps_secrets(self):
        self.assertEqual(ceaser_cipher.word_reserve(1,"a"),"b")
        self.assertEqual(ceaser_cipher.word_reserve(-1,"b"),"a")
        self.assertEqual(ceaser_cipher.word_reserve("bc","za"),None)
        self.assertEqual(ceaser_cipher.word_reserve(1,"1ertyw 23ert"),None)

if __name__ == "__main__":
    unittest.main()




