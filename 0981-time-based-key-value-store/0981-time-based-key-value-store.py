class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        l, r = 0, len(self.store[key]) - 1
        while l <= r:
            mid =  (l+r) // 2
            if timestamp == self.store[key][mid][1]:
                return self.store[key][mid][0]
            elif timestamp < self.store[key][mid][1]:
                r = mid - 1
            else:
                l = mid + 1

        if r != -1:
            return self.store[key][r][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)