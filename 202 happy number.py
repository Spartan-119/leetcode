class Solution:
    def sumOfSquare(self, n: int) -> int:
        sum = 0
        while n:
            temp = n % 10
            sum += temp * temp
            n //= 10
        return sum

    def isHappy1(self, n: int) -> bool:
        # not using the Floyd Cycle Detection Algo
        if n == 1:
                return True
                
        lookup = {}
        
        while n != 1:                       
            if n not in lookup:
                lookup[n] = 1
            else:
                return False

            # update n
            n = self.sumOfSquare(n)
            print(n)

            if n == 1:
                return True
            
    # usign the Floyd Cycle Detection Algo        
    def isHappy2(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquare(n)

        while slow != fast:
            slow = self.sumOfSquare(slow)
            fast = self.sumOfSquare(self.sumOfSquare(fast))
        
        return slow == 1

# driver method
if __name__ == '__main__':
    s = Solution()
    print(s.isHappy2(2))