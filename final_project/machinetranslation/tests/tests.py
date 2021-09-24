import unittest

from translator import french_to_english,english_to_french


class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french(""),'Bonjour') 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')       
        

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english(""),'Hello') 
        self.assertEqual(french_to_english('Bonjour'),'Hello') 
        
        
unittest.main()