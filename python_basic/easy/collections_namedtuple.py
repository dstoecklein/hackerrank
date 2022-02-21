# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple, defaultdict

if __name__ == "__main__":
    n = int(input())
    col_names = input().split()    
    sum_marks = 0
    for i in range(n):
        Student = namedtuple("Student", col_names)
        f1, f2, f3, f4 = input().split()
        s1 = Student(f1, f2, f3, f4)
        sum_marks += int(s1.MARKS)
    print(sum_marks / n)

    