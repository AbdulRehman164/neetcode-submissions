class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(speed)):
            cars.append((position[i], speed[i]))
        cars.sort()

        times = []
        for p, s in cars:
            times.append((target - p) / s)

        stack = []
        for time in reversed(times):
            top = stack[-1] if len(stack) > 0 else 0
            if time > top:
                stack.append(time)
        return len(stack)
