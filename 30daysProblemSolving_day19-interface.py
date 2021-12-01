

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        pass
        divisor = []
        
        for i in range(1,n+1):
            if n % i == 0:
                divisor.append(i)
        
        return sum(divisor)

