class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l = []
        s = self.helper(a, b, "0", l)[::-1]
        return "".join(s)

    def helper(self, a, b, carry, l):
        if len(a) == 0 and len(b) == 0:
            if carry == "1":
                l.append("1")
            return l
        if len(a) == 0:
            a = "0"
        if len(b) == 0:
            b = "0"
        l.append(str(int(a[-1]) ^ int(b[-1]) ^ int(carry)))
        if a[-1] == "0":
            carry = str(int(b[-1]) & int(carry))
        else:
            carry = str(int(b[-1]) | int(carry))
        return self.helper(a[:-1], b[:-1], carry, l)
