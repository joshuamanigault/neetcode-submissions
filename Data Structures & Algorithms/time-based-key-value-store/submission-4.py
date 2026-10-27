class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value, timestamp))
        else:
            self.map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        prev = None
        value_list = self.map[key]
        l, r = 0, len(value_list) - 1

        while l <= r:
            mid = (l + r) // 2
            if value_list[mid][1] == timestamp:
                return value_list[mid][0]
            elif value_list[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                if prev == None:
                    prev = value_list[mid]
                elif value_list[mid][1] > prev[1]:
                    prev = value_list[mid]
        
        if prev != None:
            return prev[0]
        else:
            return ""

