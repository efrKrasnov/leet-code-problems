from main import Solution


def test_1():
    s = Solution()
    nums = [1,1,1,2,2,3]
    assert s.removeDuplicates(nums) == 5
    assert nums[:5] == [1,1,2,2,3]
    
    
def test_2():
    s = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    assert s.removeDuplicates(nums) == 7
    assert nums[:7] == [0,0,1,1,2,3,3]
    