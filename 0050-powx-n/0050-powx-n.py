class Solution:
    def myPow(self, x: float, n: int) -> float:

            # 1a -> Base Case 1
            if n == 0:
                return 1
            
            # 1b -> Base Case 2
            if n == 1:
                return x
            
            # 1c -> Base Case 3
            if n == -1:
                return 1/x
            
            # 1d -> Recursive Case
            calc = self.myPow(x, n // 2)
            return calc * calc * self.myPow(x, n % 2)
        
        