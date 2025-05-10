class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        ops_count = 0
        grid_plain = [item for grid_row in grid for item in grid_row]
        grid_plain.sort()
        median_item = self.get_median_item(grid_plain)
        
        for item in grid_plain:
            if (median_item - item) % x:
                ops_count = -1
                break
            else:
                ops_count += (abs(median_item - item) // x)
        
        return ops_count

    @staticmethod
    def get_median_item(target: list[int]) -> int:
        list_len = len(target)
        assert list_len > 0
        print(f'res={target[list_len // 2]}')
        return target[list_len // 2]