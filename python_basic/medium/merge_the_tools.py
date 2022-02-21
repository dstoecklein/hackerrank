def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        print("".join(dict.fromkeys(string[i:i+k])))
   
if __name__ == '__main__':
    string, k = "AABCAAADA", 3
    merge_the_tools(string, k)
