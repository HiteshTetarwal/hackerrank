# cook your dish here
def hisrecipe(recipe):
    dish = {}
    for i in range(len(recipe)):
        if recipe[i] not in dish:
            dish[recipe[i]] = 1 
        elif recipe[i-1]==recipe[i]:
            dish[recipe[i]]+=1 
        elif recipe[i-1]!=recipe[i] and recipe[i] in dish:
            return "NO"
            
    for values in dish.values():
        if values not in indgredient_count:
            indgredient_count[values]=1
        else:
            return "NO"
    
    return "YES"
    
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = int(input())
        arr = list(map(int, input().split()))
        result = hisrecipe(arr)
        print(result)