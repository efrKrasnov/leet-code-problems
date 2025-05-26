from main import Solution


def test_1():
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") is True
    
    
def test_2():
    s = Solution()
    assert s.isAnagram('rat', 'car') is False