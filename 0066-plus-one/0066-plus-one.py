class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # 1
        num = ""

        # 2
        for digit in digits:
            num += str(digit)
        
        # 3
        num = int(num)

        # 4
        num += 1

        # 5
        result = []

        # 6
        while num:
            result.append(num % 10)
            num = num // 10
        
        # 7
        result.reverse()
        return result