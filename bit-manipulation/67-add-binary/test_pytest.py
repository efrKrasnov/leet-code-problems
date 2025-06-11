from main import Solution

def test_1():
    s = Solution()
    assert s.addBinary('11', '1') == "100"
    
    
def test_2():
    s = Solution()
    assert s.addBinary('1010', '1011') == "10101"