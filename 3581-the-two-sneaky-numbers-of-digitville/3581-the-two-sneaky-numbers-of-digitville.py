from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counted = Counter(nums)
        answer = []
        for num, count in counted.items():
            if count > 1:
                answer.append(num)
        return answer