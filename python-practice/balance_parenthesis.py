def balance_check(s):
    ''' Checks whether the braces are complete or not '''

    # Check if even number of brackets
    if len(s)%2 != 0:
        return False
    
    # Set of opening brackets
    opening = set('([{') 
    
    # Matching Pairs
    matches = set([ ('(',')'), ('[',']'), ('{','}') ]) 
    
    # Use a list as a "Stack"
    stack = []
    
    # Check every parenthesis in string
    for paren in s:
        
        # If its an opening, append it to list
        if paren in opening:
            stack.append(paren)
        
        else:
            
            # Check that there are parentheses in Stack
            if len(stack) == 0:
                # return False
                return 'NO'
            
            # Check the last open parenthesis
            last_open = stack.pop()
            
            # Check if it has a closing match
            if (last_open,paren) not in matches:
                # return False
                return 'Parenthesis not balanced.'
            
    # return len(stack) == 0
    return 'Parenthesis balanced.'

def braces(values):
    lst_ = []
    for val in values:
        res = balance_check(val)
        lst_.append(res)
    return lst_

if __name__ == '__main__':
    result = balance_check('([{)')
    print(result)