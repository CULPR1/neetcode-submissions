class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)

            else:
                if temperatures[i] <= temperatures[stack[-1]]:
                    stack.append(i)
                else:
                    while len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]:
                        popped = stack.pop()
                        result[popped] = i - popped

                    stack.append(i)

            

        return result
