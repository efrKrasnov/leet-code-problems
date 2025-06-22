from main import Solution


def test_1():
    s = "abcdefghi"
    k = 3
    fill = "x"
    
    solution = Solution()
    assert solution.divideString(s, k, fill) == ["abc","def","ghi"]
    
    
def test_2():
    s = "abcdefghij"
    k = 3
    fill = "x"
    
    solution = Solution()
    assert solution.divideString(s, k, fill) == ["abc","def","ghi", "jxx"]