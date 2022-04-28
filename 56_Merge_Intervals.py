class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        answer = [sorted_intervals[0]]
        for interval in sorted_intervals[1:]:
            if interval[0] <= answer[-1][1]:
                answer[-1][1] = max(interval[1], answer[-1][1])
            else:
                answer.append(interval)
        return answer