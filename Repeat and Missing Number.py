
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        m=0
        r=0
        A = sorted(A)
        l=set()
        for i in A:
            if i in l:
                r = i
            else:
                l.add(i)
        l=list(l)
        if l[0] != 1:
            m =1
        else:
            if len(l) == 1 and len(A) ==2:
                m = 2
            else:
                for i in range(1, len(l)):  
                    if l[i] != l[i-1]+1:
                        m = l[i-1]+1
        return [r,m]
