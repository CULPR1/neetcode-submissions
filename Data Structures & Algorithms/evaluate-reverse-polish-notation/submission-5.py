class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        op_arr = ["+","-","/","*"]
        for i in range(n):
            if tokens[i] not in op_arr:
                stack.append(int(tokens[i]))

            else:
                int_2 = stack.pop()
                int_1 = stack.pop()
                val = 0
                if tokens[i] == "+":
                    val = int_1 + int_2
                elif tokens[i] == "*":
                    val = int_1 * int_2
                elif tokens[i] == "-":
                    val = int_1 - int_2
                elif tokens[i] == "/":
                    val = int(int_1 / int_2)

                stack.append(val)
        return stack[-1]
                
