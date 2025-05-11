from main import Solution


def test_1():
    s = Solution()
    assert s.lengthOfLastWord("Hello World") == 5
    
def test_2():
    s = Solution()
    assert s.lengthOfLastWord("   fly me   to   the moon  ") == 4
    
    
def test_3():
    s = Solution()
    assert s.lengthOfLastWord("luffy is still joyboy") == 6
    