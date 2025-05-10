from main import Solution

def test_1():
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    s.rotate(nums, 3)
    assert nums == [5,6,7,1,2,3,4]
    
    
def test_2():
    s = Solution()
    nums = [3,99,-1,-100]
    s.rotate(nums, 2)
    assert nums == [-1,-100,3,99]
    
    
def test_3():
    s = Solution()
    nums = [1,2,3,4,5,6]
    s.rotate(nums, 3)
    assert nums == [4,5,6,1,2,3]
