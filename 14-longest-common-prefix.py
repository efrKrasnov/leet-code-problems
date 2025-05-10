class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix_str = strs[0]
        slice_pos = 0
        is_correct_prefix = True
        for i in range(len(prefix_str)):
            for j in range(len(strs)):
                if i < len(strs[j]) and prefix_str[i] == strs[j][i]:
                    pass
                else:
                    is_correct_prefix = False
                    break
            if is_correct_prefix:
                slice_pos += 1
            else:
                break
        print(prefix_str[:slice_pos])
        return prefix_str[:slice_pos]
            
                    
    
    
if __name__ == '__main__':
    s = Solution()
    assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert s.longestCommonPrefix(["dog","racecar","car"]) == ""
    assert s.longestCommonPrefix(["ab", "a"]) == "a"