def pathSum(self, A, B):
        if A==None:
            return
        sa=[]
        t=[]
        sa=self.check(A,B,sa,t)
        return sa
    def check(self,A,B,sa,t):
        if A is None:
            return sa
        if (A.left is None) and (A.right is None) and (B==A.val):
            t.append(A.val)
            s=t[:]
            sa.append(s)
            return sa
        t.append(A.val)
        if A.left is not None:
            s=t[:]
            sa=self.check(A.left,B-A.val,sa,s)
        if A.right is not None:
            s=t[:]
            sa=self.check(A.right,B-A.val,sa,s)
        return sa
