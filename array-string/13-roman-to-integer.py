class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            match s[i]:
                case "M":
                    result += 1000
                    i += 1
                case "D":
                    result += 500
                    i += 1
                case "L":
                    result += 50
                    i += 1
                case "V":
                    result += 5
                    i += 1
                case "C":
                    if i < len(s) - 1 and s[i + 1] == "D":
                        result += 400
                        i += 2
                    elif i < len(s) - 1 and s[i + 1] == "M":
                        result += 900
                        i += 2
                    else:
                        result += 100
                        i += 1
                case "X":
                    if i < len(s) - 1 and s[i + 1] == "L":
                        result += 40
                        i += 2
                    elif i < len(s) - 1 and s[i + 1] == "C":
                        result += 90
                        i += 2
                    else:
                        result += 10
                        i += 1
                case "I":
                    if i < len(s) - 1 and s[i + 1] == "V":
                        result += 4
                        i += 2
                    elif i < len(s) - 1 and s[i + 1] == "X":
                        result += 9
                        i += 2
                    else:
                        result += 1
                        i += 1
        print(result)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
