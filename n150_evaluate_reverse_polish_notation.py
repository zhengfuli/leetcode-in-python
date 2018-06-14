class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        for op in tokens:
            if op not in ["+", "-", "*", "/"]:
                nums.append(op)
            else:
                b, a = int(nums.pop()), int(nums.pop())

                if op == "+":
                    nums.append(a + b)
                elif op == "-":
                    nums.append(a - b)
                elif op == "*":
                    nums.append(a * b)
                elif op == "/":
                    if a * b < 0:
                        nums.append(-(abs(a) / abs(b)))
                    else:
                        nums.append(a / b)

        return int(nums.pop())