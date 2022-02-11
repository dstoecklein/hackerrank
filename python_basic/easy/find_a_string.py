def count_substring(string, sub_string):
    counter = 0
    for _ in string:

        if len(string) < len(sub_string):
            break

        for i, c_sub in enumerate(sub_string):
            if (c_sub.isupper() and string[i].islower()) or (c_sub.islower() and string[i].isupper()):
                break

            if c_sub == string[i]:
                counter += 1

        string = string[1:]
  
    return int(counter / len(sub_string))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)