class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_to_word: dict[str, str] = {}
        word_to_char: dict[str, str] = {}
        
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        for i, char in enumerate(pattern):
            word = words[i]
            if char not in char_to_word and word not in word_to_char:
                char_to_word[char] = word
                word_to_char[word] = char               
                
            if char_to_word.get(char) != word and word_to_char.get(word) != char:
                return False
                
        return True