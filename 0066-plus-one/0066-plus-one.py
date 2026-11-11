class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        sum=0
        ar=[]
        ar2=[]
        for i in digits:
            sum=(sum+i)*10
        sum=(sum//10)+1


        while sum>0:
            s=sum%10
            sum=sum//10
            ar.append(s)
            


        return(ar[::-1])

        

        