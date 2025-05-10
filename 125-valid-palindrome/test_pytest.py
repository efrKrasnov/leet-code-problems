from main import Solution


def test_1():
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") is True
    

def test_2():
    s = Solution()
    assert s.isPalindrome("race a car") is False
    
    
def test_3():
    s = Solution()
    assert s.isPalindrome(" ") is True
    
    
def test_4():
    s = Solution()
    assert s.isPalindrome("a.") is True
    
    
def test_5():
    s = Solution()
    assert s.isPalindrome(".,") is True
    
    
def test_6():
    s = Solution()
    assert s.isPalindrome("0P") is False