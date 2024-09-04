

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {
    (91, 100): "Outstanding",
    (81, 90): "Exceeds Expectations", 
    (71, 80): "Acceptable",
    (0, 70): "Fail"
}
    

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}



student_grades = {}

for student in student_scores:
    scores = student_scores[student]
    if scores > 90:
        student_grades[student] = "Outstanding"
    elif scores > 80:
        student_grades[student] = "Exceeds Expectations"
    elif scores > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)

for student, grades in student_grades.items():
    print(f'{student}: {grades}')


