class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        below_ten = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        ten_to_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                         "Eighteen", "Nineteen"]
        below_hundreds = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if num < 0 or num > 2 ** 31 - 1: return
        words = ""
        queue = [num]

        while queue:
            # print(queue)
            num = queue.pop()

            if type(num) == str:
                words += num

            elif num == 0 and words != "":
                pass

            elif num >= 1e9:
                queue.append(num % 1e9)
                queue.append(" Billion")
                queue.append(num // 1e9)

            elif 1e9 > num >= 1e6:
                queue.append(num % 1e6)
                queue.append(" Million")
                queue.append(num // 1e6)

            elif 1e6 > num >= 1e3:
                queue.append(num % 1e3)
                queue.append(" Thousand")
                queue.append(num // 1e3)

            elif 1e3 > num >= 1e2:
                queue.append(num % 1e2)
                queue.append(" Hundred")
                queue.append(num // 1e2)

            elif 1e2 > num >= 20:
                queue.append(num % 10)
                queue.append(" " + below_hundreds[int((num // 10) - 2)])

            elif 20 > num >= 10:
                words += " " + ten_to_twenty[int(num % 10)]

            else:
                words += " " + below_ten[int(num)]

        return words.lstrip(" ")


