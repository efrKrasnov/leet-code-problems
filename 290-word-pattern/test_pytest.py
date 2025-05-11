from main import Solution


def test_1():
    s = Solution()
    assert s.wordPattern("abba", "dog cat cat dog") is True
    
    
def test_2():
    s = Solution()
    assert s.wordPattern("abba", "dog cat cat fish") is False
    
    
def test_3():
    s = Solution()
    assert s.wordPattern("aaaa", "dog cat cat dog") is False
    