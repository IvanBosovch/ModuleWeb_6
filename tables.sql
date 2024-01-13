-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups(
    id INTEGER PRIMARY KEY,
    group_name VARCHAR(30) 
);


-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    students_name VARCHAR(50) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
);


-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teachers_name VARCHAR(50)
);


-- Table: disciplines
DROP TABLE IF EXISTS disciplines;
CREATE TABLE disciplines(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_disciplines VARCHAR(20) NOT NULL,
    id_teacher INTEGER,
    FOREIGN KEY (id_teacher) REFERENCES teachers (id)
);


-- Table: grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    discipline_id INTEGER,
    grade INTEGER NOT NULL,
    date_grade DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (discipline_id) REFERENCES disciplines (id)
);

