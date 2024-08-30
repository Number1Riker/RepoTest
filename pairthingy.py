import unittest

class Guy:
    def __init__(self):
        self.Name = ""

    def speak(self, words):
        print(words)
        return words

    def myName(self, name):
        self.Name = name

class LoudGuy(Guy):
    def yell(self, words):
        print(words.upper())
        return words.upper()

class TestStringMethods(unittest.TestCase): 
    def test_guyTest(self):
        testGuy = Guy()
        testGuy.myName("Man")
        self.assertEqual("Man", testGuy.Name)
        self.assertEqual("I am me", testGuy.speak("I am me"))
    
    def test_LoudTest(self):
        testLoud = LoudGuy()
        testLoud.myName("LoudMan")
        self.assertEqual("LoudMan", testLoud.Name)
        self.assertEqual("I am me", testLoud.speak("I am me"))
        self.assertEqual("I AM ME", testLoud.yell("I am me"))

if __name__ == '__main__': 
    unittest.main()