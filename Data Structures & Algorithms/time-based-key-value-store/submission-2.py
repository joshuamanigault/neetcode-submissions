class TimeMap:

    def __init__(self):
        self.map = {

        }
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value, timestamp))
        else:
            self.map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        prev = None
        l, r = 0, len(self.map[key]) - 1

        while l <= r:
            mid = (l + r) // 2
            temp = self.map[key][mid]
            if temp[1] == timestamp:
                return temp[0]
            elif temp[1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                if prev == None:
                    prev = temp
                elif temp[1] > prev[1]:
                    prev = temp
        

        if prev != None:
            return prev[0]
        else:
            return ""