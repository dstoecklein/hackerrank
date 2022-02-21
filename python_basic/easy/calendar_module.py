# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

if __name__ == '__main__':
    m, d, y = input().split()
    day_idx = calendar.weekday(int(y), int(m), int(d))
    print(str(list(calendar.day_name)[day_idx]).upper())