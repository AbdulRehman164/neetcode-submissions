class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort()

        times = []
        for car in cars:
            times.append((target - car[0]) / car[1])

        fleets = 1
        stack = []
        for time in reversed(times):
            if stack and time > stack[-1]:
                fleets += 1
                stack.clear()
            if not stack:
                stack.append(time)
        return fleets
