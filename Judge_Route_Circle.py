class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for i in moves:
            if i is "U":
                y+=1
            elif i is "D":
                y-=1
            elif i is "L":
                x-=1
            elif i is "R":
                x+=1
            else:
                return False
        if x==0 and y==0:
            return True
        return False
