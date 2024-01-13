SELECT t.teachers_name, d.name_disciplines, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g 
JOIN disciplines d ON d.id = g.discipline_id 
JOIN teachers t ON t.id = d.id_teacher 
WHERE t.id  = 1
GROUP BY d.name_disciplines
ORDER BY average_grade DESC;