# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
# for every line, call input()
for i in range(int(input())):
    block_size = int(input())
    block = list(map(int, input().split()))
    
    if 1 <= block_size <= sys.maxsize:
        idx_of_minimum = block.index(min(block))
        
        block_left_sliced = block[:idx_of_minimum]
        block_right_sliced = block[idx_of_minimum+1:]
        
        if block_left_sliced == sorted(block_left_sliced, reverse=True) and block_right_sliced == sorted(block_right_sliced):
            print("Yes")
        else:
            print("No")