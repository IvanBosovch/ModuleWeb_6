SELECT students.id, students.students_name, ROUND(AVG(grades.grade), 2) as average_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id, students.students_name
ORDER BY average_grade DESC
LIMIT 5;