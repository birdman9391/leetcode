import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = bisect.bisect_left(intervals, newInterval[0], key=lambda x:x[0])
        intervals.insert(index, newInterval)
        
        if index - 1 >= 0 and intervals[index - 1][1] >= intervals[index][0]:
            intervals[index - 1][1] = max(intervals[index - 1][1], intervals[index][1])
            del intervals[index]
            index -= 1

        while index + 1 < len(intervals):
            if intervals[index][1] >= intervals[index + 1][0]:
                intervals[index][1] = max(intervals[index][1], intervals[index + 1][1])
                del intervals[index + 1]
            else:
                break
        return intervals