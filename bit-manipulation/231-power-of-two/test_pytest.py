from main import Solution


def test_1():
    s = Solution()
    assert s.isPowerOfTwo(1) is True


def test_2():
    s = Solution()
    assert s.isPowerOfTwo(16) is True
    
    
def test_3():
    s = Solution()
    assert s.isPowerOfTwo(3) is False
    