from typing import DefaultDict


class TimeMap:
    def __init__(self):
        self.data = DefaultDict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        values = self.data[key]
        L, R = 0, len(values) - 1
        while L <= R:
            mid = (L + R) // 2
            if timestamp > values[mid][0]:
                L = mid + 1
            elif timestamp < values[mid][0]:
                R = mid - 1
            else:
                return values[mid][1]
        return values[R][1] if R >= 0 and values[R][0] < timestamp else ""
