class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        res1 = "Fizz"
        res2 = "Buzz"
        for i in range(int(n)):
            k = i + 1
            tmp = ""
            if k % 15 == 0:
                tmp = tmp + res1 +res2
            elif k % 3 == 0:
                tmp = tmp + res1
            elif k % 5 == 0:
                tmp = tmp + res2
        
            else:
                tmp = str(k)
            res.append(tmp)
        return res