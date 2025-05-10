from main import Solution


def test_1():
    s = Solution()
    assert s.minimumIndex([1,2,2,2]) == 2
    
    
def test_2():
    s = Solution()
    assert s.minimumIndex([2,1,3,1,1,1,7,1,2,1]) == 4
    
    
def test_3():
    s = Solution()
    assert s.minimumIndex([3,3,3,3,7,2,2]) == -1