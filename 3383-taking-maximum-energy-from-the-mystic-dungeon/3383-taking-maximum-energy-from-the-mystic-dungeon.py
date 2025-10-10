class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ps = energy[:]
        for i in range(k, len(ps)):
            ps[i] = max(ps[i], ps[i]+ps[i-k])
    
        return max(ps[-k:])