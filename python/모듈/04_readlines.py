with open('student.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    print(lines, type(lines))