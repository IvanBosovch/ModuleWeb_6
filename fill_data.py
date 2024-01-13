import faker
import sqlite3
from random import randint
from datetime import datetime

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 4
NUMBER_DISCIPLINES = 5
NUMBER_TEACHERS = 3
NUMBER_GRADES = 20

def generate_fake(students, groups, disciplines, teachers):
    fake_students = []
    fake_groups = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    fake_disciplines = ['Mathematics', 'Biologi', 'English', 'Statistic', 'History of Ukraine']
    fake_teachers =[]
    fake_data = faker.Faker()

    for _ in range(students):
        fake_students.append(fake_data.name())

    for _ in range(teachers):
        fake_teachers.append(fake_data.name())

    return fake_students, fake_groups, fake_disciplines, fake_teachers


def prepare_data(students, groups, disciplines, teachers):
    for_groups = []
    for group in groups:
        for_groups.append((group, ))

    for_students =[]
    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher, ))

    for_disciplines = []
    for discipline in disciplines:
        for_disciplines.append((discipline, randint(1, NUMBER_TEACHERS)))

    for_grades = []
    for student_id in range(1, NUMBER_STUDENTS + 1):
        for _ in range(1, NUMBER_GRADES + 1):
            discipline_id = randint(1, NUMBER_DISCIPLINES)
            grade = randint(50, 100)
            date_grade = datetime(randint(2022, 2023), randint(1, 12), randint(1, 28)).date()
            for_grades.append((student_id, discipline_id, grade, date_grade)) 
    
    return for_groups, for_students, for_teachers, for_disciplines, for_grades


def insert_data_to_db(groups_tb, students_tb, teachers_tb, disciplines_tb, grades_tb):
    with sqlite3.connect('Hogwatrs.db') as con:
        cur = con.cursor()

        sql_to_groups = "INSERT INTO groups(group_name) VALUES (?);"
        cur.executemany(sql_to_groups, groups_tb)

        sql_to_students = "INSERT INTO students(students_name, group_id) VALUES (?, ?)"
        cur.executemany(sql_to_students, students_tb)

        sql_to_teachers = "INSERT INTO teachers(teachers_name) VALUES (?)"
        cur.executemany(sql_to_teachers, teachers_tb)

        sql_to_disciplines = "INSERT INTO disciplines(name_disciplines, id_teacher) VALUES (?, ?)"
        cur.executemany(sql_to_disciplines, disciplines_tb)

        sql_to_grades = "INSERT INTO grades(student_id, discipline_id, grade, date_grade) VALUES (?, ?, ?, ?)"
        cur.executemany(sql_to_grades, grades_tb)

        con.commit()

if __name__ == '__main__':
    groups_tb, students_tb, teachers_tb, disciplines_tb, grades_tb = prepare_data(*generate_fake(NUMBER_STUDENTS, NUMBER_GROUPS,
                                                                                        NUMBER_DISCIPLINES, NUMBER_TEACHERS))
    insert_data_to_db(groups_tb, students_tb, teachers_tb, disciplines_tb, grades_tb)