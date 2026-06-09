from typing import DefaultDict


class TimeMap:
    def __init__(self):
        self.data = DefaultDict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        arr = self.data[key]
        L = 0
        R = len(arr) - 1

        while L <= R:
            mid = (L + R) // 2
            if arr[mid][1] > timestamp:
                R = mid - 1
            elif arr[mid][1] < timestamp:
                L = mid + 1
            else:
                return arr[mid][0]
        # if R=-1 python handles it
        return arr[R][0] if timestamp > arr[R][1] else ""
