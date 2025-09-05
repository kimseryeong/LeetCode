class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        arr = [i for i in range(1, n + 1)]
        for idx, val in enumerate(arr):
            if val % 3 == 0 and val % 5 == 0: arr[idx] = "FizzBuzz"
            elif val % 3 == 0: arr[idx] = "Fizz"
            elif val % 5 == 0: arr[idx] = "Buzz"
            else: arr[idx] = str(val)
        return arr
    
        