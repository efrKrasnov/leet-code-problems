from main import Solution

def test_1():
    s = Solution()
    assert s.isSubsequence("abc", "ahbgdc") is True
    
def test_2():
    s = Solution()
    assert s.isSubsequence("axc", "ahbgdc") is False
    
def test_3():
    s = Solution()
    assert s.isSubsequence("b", "v") is False
    