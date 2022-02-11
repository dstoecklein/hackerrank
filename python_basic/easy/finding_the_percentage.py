if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    n = 0.00
    for i in student_marks[query_name]:
        n += i
        
    print("{:.2f}".format(n/len(student_marks[query_name])))