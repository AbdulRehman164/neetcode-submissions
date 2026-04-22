class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars.sort()

        times = []
        for car in cars:
            times.append((target - car[0]) / car[1])

        stack = []
        for time in reversed(times):
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
