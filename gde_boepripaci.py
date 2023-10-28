cv = open('students.txt')
students = []
for student in cv:
    line = student.split(';')
    students.append({'id':int(line[0]), 'name':line[1], 'var':int(line[2]), 'subgroup':int(line[3])})

student1, _, _, student4, *_, lastStudent = students
*new_students, = student1, student4, lastStudent
print(new_students)

cv.close()