SELECT s.students_name, g2.group_name, d.name_disciplines, g.grade 
FROM grades g
JOIN students s ON s.id = g.student_id 
JOIN groups g2 ON s.group_id = g2.id 
JOIN disciplines d ON d.id = g.discipline_id 
WHERE g2.id = 1 and d.id = 1
ORDER BY s.students_name;