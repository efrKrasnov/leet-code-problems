from main import Solution


def test_1():
    word = "aabcaba"
    k = 0
    
    s = Solution()
    assert s.minimumDeletions(word, k) == 3
    
    
def test_2():
    word = "dabdcbdcdcd"
    k = 2
    
    s = Solution()
    assert s.minimumDeletions(word, k) == 2
    
    
def test_3():
    word = "aaabaaa"
    k = 2
    
    s = Solution()
    assert s.minimumDeletions(word, k) == 1
    