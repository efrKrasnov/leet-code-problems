class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        counters_per_word: dict[str, dict[str, int]] = {}

        for word in words:
            chars_in_word = {}
            for char in word:
                if char not in chars_in_word:
                    chars_in_word[char] = 1
                else:
                    chars_in_word[char] += 1
            counters_per_word[word] = chars_in_word

        result_counters = {}

        test_word = counters_per_word[words[0]]
        for char in test_word:
            counters_per_char = []
            is_all_words_listed = True
            for word in counters_per_word:
                if char in counters_per_word[word]:
                    counters_per_char.append(counters_per_word[word][char])
                else:
                    is_all_words_listed = False
                    break

            if not is_all_words_listed:
                continue
            else:
                result_counters[char] = min(counters_per_char)

        result = []
        for char in result_counters:
            for _ in range(result_counters[char]):
                result.append(char)

        return result
