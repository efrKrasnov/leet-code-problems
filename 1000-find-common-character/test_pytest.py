from main import Solution


def test_1():
    s = Solution()
    result = s.commonChars(["bella","label","roller"])
    assert result.count('e') == 1
    assert result.count('l') == 2
    
    
def test_2():
    s = Solution()
    result = s.commonChars(["cool","lock","cook"])
    assert result.count('c') == 1
    assert result.count('o') == 1