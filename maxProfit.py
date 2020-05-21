"""
class Solution:
    def maxProfit(self, prices):
        profit_made=[]
        new_high=0
        for i in range(len(prices)):
            count=0
            for j in range(i+1,len(prices)):
                count=count+1
                if j+1==len(prices):
                    new_high=prices[j]-prices[i]
                    print(new_high)
                    profit_made.append(new_high)
                    break
                if prices[j]<prices[j+1]:
                    continue
                # elif j==len(prices)-1:
                elif prices[j]>prices[j-1] and prices[j]>prices[j+1]:
                        new_high=prices[j]-prices[i]
                        print(new_high)
                        profit_made.append(new_high)
                count=count+1
            if count==len(prices)-1:
                break

        max_profit=0   
        print(profit_made)
        for i in range(0,len(profit_made)):
            max_profit+=profit_made[i]
        return max_profit

"""

                    
if __name__=="__main__":
    arr = [1,2,3,4,5]
    print(arr)
    n = len(arr)
    obj1=Solution()
    print(obj1.maxProfit(arr))

        
                    

















                    # if prices[j]>prices[i] and prices[j]>prices[j+1]:
                    #     new_high=prices[j]-prices[i]
                    #     profit_made.append(new_high)
                    #     print(new_high)
                    #     if j<len(prices)-2:
                    #         i=j+1
                    # elif prices[j]>prices[i] and prices[j]<prices[j+1]:
                    #     j=j+1