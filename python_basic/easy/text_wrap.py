import textwrap
from typing import overload

# without textwrap
def wrap(string, max_width):
    string_list = list(string)
    split_list = list()
    
    for i in range(0, len(string_list), max_width):
        split_list.append("".join(string_list[i:i+max_width])+"\n")
        
    return "".join(split_list)

# with textwrap (actual solution)
def wrap2(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap2(string, max_width)
    print(result)