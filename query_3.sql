SELECT g2.group_name, d.name_disciplines, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN disciplines d ON d.id = g.discipline_id 
JOIN groups g2 ON g2.id = s.group_id
WHERE d.id = 3
GROUP BY g2.group_name, d.name_disciplines 
ORDER BY average_grade DESC;