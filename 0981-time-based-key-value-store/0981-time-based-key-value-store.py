class TimeMap:

    def __init__(self):
        self.key_ts = {}
        self.ts_val = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_ts.setdefault(key, []).append(timestamp)

        self.ts_val[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_ts:
            return ""

        ts = self.key_ts[key]
        # ts.sort()
        l, r = 0, len(ts)-1

        while l <= r:
            mid = (l+r) // 2
            if timestamp == ts[mid]:
                r = mid
                break
            if timestamp >  ts[mid]:
                l = mid+1
            elif timestamp < ts[mid]:
                r = mid-1

        if r < 0:
            return ""
      
        return self.ts_val[ts[r]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)