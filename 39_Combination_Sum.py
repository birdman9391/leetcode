class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def _combinationSum(sorted_candidates, cur_candidates, target):
            answer = []
            l = len(sorted_candidates)
            prev = -1
            for i in range(l-1, -1, -1):
                # print(sorted_candidates, cur_candidates, target)
                # if sorted_candidates[i] == prev:
                #     continue
                    
                
                if sorted_candidates[i] == target:
                    answer.append(cur_candidates + [sorted_candidates[i]])
                    # prev = sorted_candidates[i]
                elif sorted_candidates[i] < target:
                    answer = answer + _combinationSum(sorted_candidates[:i+1], cur_candidates + [sorted_candidates[i]], target - sorted_candidates[i])
                    # prev = sorted_candidates[i]
            # print(answer)
            return answer

        candidates.sort()
        return _combinationSum(candidates, [], target)
        
            