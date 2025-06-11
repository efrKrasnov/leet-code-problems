from main import Solution

def test_1():
    s = Solution()
    assert s.reverseBits(43261596) == 964176192
    
    
def test_2():
    s = Solution()
    assert s.reverseBits(4294967293) == 3221225471