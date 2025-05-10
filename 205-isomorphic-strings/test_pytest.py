from main import Solution

def test_1():
    s = Solution()
    assert s.isIsomorphic("egg", "add") is True
    
    
def test_2():
    s = Solution()
    assert s.isIsomorphic("foo", "bar") is False
    
    
def test_3():
    s = Solution()
    assert s.isIsomorphic("paper", "title") is True
    
    
def test_4():
    s = Solution()
    assert s.isIsomorphic("badc", "baba") is False