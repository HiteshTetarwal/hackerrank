# The game consists of one or more turns. In each turn:

# If both TS and JS are even, their values get divided by 2 and the game proceeds with the next turn.
# If both TS and JS are odd, a tie is declared and the game ends.
# If TS is even and JS is odd, Tom wins the game.
# If TS is odd and JS is even, Jerry wins the game.

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


def jerry_win(ts):
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


    q = int(input())
    for q_itr in range(q):
        n = int(input())
        result = jerry_win(n)
        print(result)