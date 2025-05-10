class Solution():
    def partitionLabels(self, s: str) -> list[int]:
        class Partition:
            def __init__(self, length: int, chars: set[str]):
                self.length: int = length
                self.chars: set[str] = chars
                
            def __repr__(self):
                return f'Partition length {self.length}, chars {self.chars}'
                
        partitions: list[Partition] = []
        
        for char in s:
            ep_pos = -1
            for i in range(len(partitions)):
                if char in partitions[i].chars:
                    ep_pos = i
                    break
                
            if ep_pos < 0:
                partitions.append(Partition(1, {char}))
            else:
                if partitions[ep_pos] == partitions[-1]:
                    partitions[ep_pos].chars.add(char)
                else:
                    r_pos = len(partitions) - 1
                    while r_pos > ep_pos:
                        partitions[ep_pos].length += partitions[r_pos].length
                        partitions[ep_pos].chars.update(partitions[r_pos].chars)
                        partitions.pop()
                        r_pos -= 1
                partitions[ep_pos].length += 1
                    
        return [partition.length for partition in partitions]
    