grade_one= {'Sami': [19, 18, 19.5, 30, 10],
            'Ahmad': [15, 14, 16, 21, 7],
            'Faris': [18, 19, 17, 26, 9],
            'Salem': [20, 20, 19, 30, 10],
            'Mahmoud': [12, 13, 11, 18, 7]}
grade_two= {'Lana': [17, 19, 20, 28, 9],
            'Dina': [18.5, 19.5, 20, 29, 10],
            'Maha': [20, 20, 18, 26, 9],
            'Abeer': [16, 18, 19.5, 25, 8]}
grade_three= {'Rima': [18, 19, 18, 26, 9],
              'Tala': [20, 20, 19, 29, 10],
              'Lamar': [19, 20, 18, 26, 9],
              'Rola': [15, 14, 16, 19, 7],
              'Naya': [9, 6, 11, 14, 7],
              'Dalal': [1, 5, 2, 6, 7],
              'Ola': [19.5, 20, 20, 29.5, 10]}
def students_names():
    grade= input('Enter grade: ')
    a= list(grade.keys())
    print(a)

def students_score():
    grade, name = input('Enter grade: '), input('Enter name: ')
    a= sum(grade[name])
    print(a)

def students_count():
    grade= input('Enter grade: ')
    a= len(list(grade.keys()))
    print(a)

print('Choose one: students_names(), students_score(), students_count()')
x= input('Choose one: ')
y= input("If you finished write 'Done' or If you not write 'More': ")
while True:
    if y=='More':
        print('Choose one: students_names, students_score, students_count')
        x= input('Choose one: ')
        y= input("If you finished write 'Done' or If you not write 'More': ")
    else:
        break
