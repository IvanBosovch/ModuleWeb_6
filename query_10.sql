SELECT s.students_name, d.name_disciplines, t.teachers_name
FROM grades g 
JOIN disciplines d ON d.id = g.discipline_id 
JOIN students s ON s.id = g.student_id
JOIN teachers t ON t.id = d.id_teacher 
WHERE s.id = 1 and t.id = 2;