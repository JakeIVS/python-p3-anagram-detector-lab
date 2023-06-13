# your code goes here!
class Anagram():
    pass
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        anagrams = []
        for word in word_list:
            if sorted([letter for letter in word]) == sorted([letter for letter in self.word]):
                anagrams.append(word)

        return anagrams
