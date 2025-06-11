from main import Solution


def test_1():
    s = Solution()
    assert s.hammingWeight(11) == 3
    
def test_2():
    s = Solution()
    assert s.hammingWeight(128) == 1
    
    
def test_3():
    s = Solution()
    assert s.hammingWeight(2147483645) == 30
    
    