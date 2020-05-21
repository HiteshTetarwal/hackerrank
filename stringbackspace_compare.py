class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        newS=[]
        newT=[]
        for i in range(len(S)):
            if S[i]=="#" and (i==0 or len(newS)==0):
                continue
            if S[i]=="#":
                newS.pop()
            else:
                newS.append(S[i])
        for j in range(len(T)):
            if T[j]=="#" and (j==0 or len(newT)==0):
                continue
            if T[j]=="#":
                newT.pop()
            else:
                newT.append(T[j])
        
        if newS == newT:
            return True
        else:
            return False

