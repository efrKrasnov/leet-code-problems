from main import Solution


def test_1():
    s = Solution()
    assert s.minOperations([[2,4],[6,8]], 2) == 4
    
    
def test_2():
    s = Solution()
    assert s.minOperations([[1,5],[2,3]], 1) == 5
    
    
def test_3():
    s = Solution()
    assert s.minOperations([[1,2],[3,4]], 2) == -1
    
    
def test_4():
    s = Solution()
    assert s.minOperations([[146]], 86) == 0