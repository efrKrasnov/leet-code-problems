from main import Solution


def test_1():
    s = Solution()
    assert s.numberOfPowerfulInt(1, 6000, 4, "124") == 5
    
    
def test_2():
    s = Solution()
    assert s.numberOfPowerfulInt(15, 215, 6, "10") == 2
    
    
def test_3():
    s = Solution()
    assert s.numberOfPowerfulInt(1000, 2000, 4, "3000")
    