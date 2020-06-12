import math

def Log2(x): 
    if x == 0: 
        return false; 
  
    return (math.log10(x) / 
            math.log10(2)); 
def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == 
            math.floor(Log2(n)));
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
        
def is_odd(n):
    if n%2!=0:
        return True
    else:
        return False




def diff_i(ts):
    l = int(ts)
    for n in range(1,l):
        if int((2**(n))*(1+(2*int(ts/(2**(n+1))))))/ts==1:
            # print(n)
            return 2**(n+1)
    return None


#code with formula
def jerry_with_formula(ts):
    count = 0
    if is_odd(ts):
        return int(ts/2)
    elif is_even(ts):
        if isPowerOfTwo(ts):
            return 0
        else:
            n = diff_i(ts)
            if n == None:
                return 1
            else:
                return int(ts/n)       
    return count

#code with brute force
def jerry_purana(ts):
    js = 1
    count=0
    while js<ts:
        if is_even(ts) and is_odd(js):
            pass
        elif is_odd(ts) and is_even(js):
            count = count + 1
        elif is_even(ts) and is_even(js):
            ts=ts/2
            js=js/2
            continue
            
            
        js+=1
    
    return count


if __name__ == '__main__':
    khali = []
    count = 0
    # i in the following loop will be the value of tom
    for i in range(1,10000):
        result = jerry_with_formula(999)
        result2= jerry_purana(999)
        print(result2,result)
        count+=1
        if result!=result2:
            khali.append([result,result2])
        # print(result,i,count)
    print(khali)