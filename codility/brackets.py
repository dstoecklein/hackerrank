def check_str(string_):
    stack = list()

    openb = "[({" # when open -> push
    closeb = "])}" # when close -> pop
    valid = False

    if string_[0] in closeb:
        return valid
    else:   
        for c in string_:
            if c in openb:
                stack.append(c)
            if c in closeb:
                if ord(c) == 125 and ord(stack[len(stack)-1]) == 123:
                    valid = True
                elif ord(c) == 93 and ord(stack[len(stack)-1]) == 91:
                    valid = True
                elif ord(c) == 41 and ord(stack[len(stack)-1]) == 40:
                    valid = True   
                else:
                    valid = False
                    break
                stack.pop()  
            else:
                valid = False  

    return valid

str_ = "]["
print(check_str(str_))