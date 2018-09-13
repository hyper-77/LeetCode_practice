def check_valid_parentheses(s):
    dict={')':'('}
    temp=[]
    for char in s:
        if char=='(':
            temp.append(char)
        else:
            if len(temp)==0:
                return False
            last=temp.pop()
            if not last==dict[char]:
                return False

    return len(temp)==0

print(check_valid_parentheses('(()()())'))
