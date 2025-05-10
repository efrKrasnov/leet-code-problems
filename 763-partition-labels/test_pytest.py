from main import Solution


def test_1():
    s = Solution()
    assert s.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    
    
def test_2():
    s = Solution()
    assert s.partitionLabels("eccbbbbdec") == [10]