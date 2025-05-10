from main import Solution

def test_1():
    s = Solution()
    assert s.isValid("()") is True
    
    
def test_2():
    s = Solution()
    assert s.isValid("()[]{}") is True
    
    
def test_3():
    s = Solution()
    assert s.isValid("(]") is False
    
    
def test_4():
    s = Solution()
    assert s.isValid("([])") is True