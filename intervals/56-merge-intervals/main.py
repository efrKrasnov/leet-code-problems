class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for interval in intervals[1:]:
            last_interval = result[-1]
            if interval[0] <= last_interval[1]:
                if interval[1] <= last_interval[1]:
                    continue
                else:
                    last_interval[1] = interval[1]
            else:
                result.append(interval)
                
        return result