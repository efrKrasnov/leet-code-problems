from main import Solution

def test_1():
    s = Solution()
    assert s.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    
def test_2():
    s = Solution()
    assert s.merge([[1,4],[4,5]]) == [[1,5]]
    
    
def test_3():
    s = Solution()
    assert s.merge([[1,4],[0,4]]) == [[0,4]]
    
    
def test_4():
    s = Solution()
    assert s.merge([[1,4],[2,3]]) == [[1,4]]