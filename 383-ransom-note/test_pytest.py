from main import Solution

def test_1():
    s = Solution()
    assert s.canConstruct("a", "b") is False
    
    
def test_2():
    s = Solution()
    assert s.canConstruct("aa", "ab") is False
    
    
def test_3():
    s = Solution()
    assert s.canConstruct("aa", "aab") is True