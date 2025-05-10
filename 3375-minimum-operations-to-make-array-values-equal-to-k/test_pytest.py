from main import Solution

def test_1():
    s = Solution()
    assert s.minOperations([5,2,5,4,5], 2) == 2
    
def test_2():
    s = Solution()
    assert s.minOperations([2, 1, 2], 2) == -1
    
    
def test_3():
    s = Solution()
    assert s.minOperations([9,7,5,3], k=1) == 4
    
    
def test_3():
    s = Solution()
    assert s.minOperations([1], k=1) == 0