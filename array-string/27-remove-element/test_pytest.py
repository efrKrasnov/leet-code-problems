from main import Solution

def test_1():
    s = Solution()
    nums = [3,2,2,3]
    assert s.removeElement(nums, 3) == 2
    assert nums[:2] == [2, 2]
    
    
def test_2():
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    assert s.removeElement(nums, 2) == 5
    assert nums[:5] == [0,1,3,0,4]