class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + stations[i]

        power = []
        for i in range(n):
            left = max(0, i - r)
            right = min(n, i + r + 1)
            power.append(pre[right] - pre[left])

        def can(x):
            add = [0] * (n + 1)
            curr_add = 0
            used = 0
            curr_power = power[:]

            for i in range(n):
                curr_add += add[i]
                curr_power[i] += curr_add

                if curr_power[i] < x:
                    need = x - curr_power[i]
                    used += need
                    if used > k:
                        return False
                    curr_add += need
                    end = min(n, i + 2 * r + 1)
                    add[end] -= need

            return True

        low, high = 0, max(power) + k
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans