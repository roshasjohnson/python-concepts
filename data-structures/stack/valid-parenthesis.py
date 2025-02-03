
def isValid(string):
    if len(string) < 2:
        return False
    mapping = {")":"(","]":"[","}":"{"}
    stack = []
    for char in string:
        if char in mapping:
            if not stack :
                return False
            top_element= stack.pop()
            if top_element != mapping[char]:
                print(f"{top_element}:{char} " ,end = "")
                return False
        else:
            stack.append(char)
 
    return not stack

    
strings = ["((()))", "{{}}", "({{{}}})", "([)]", "(()", ""]
for s in strings:
    print(f"{s}: {isValid(s)}")

