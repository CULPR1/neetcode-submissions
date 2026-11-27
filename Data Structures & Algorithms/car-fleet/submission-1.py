class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = []
        for i in range(len(position)):
            pos.append([position[i],speed[i]])
        pos.sort()

        stack = []
        for k in pos:
            time = (target - k[0])/k[1]
            while stack and stack[-1] <= time:
                stack.pop()

            stack.append(time)

        return len(stack)