SELECT d.name_disciplines, t.teachers_name 
FROM disciplines d 
JOIN teachers t  ON t.id = d.id_teacher
WHERE t.id = 2
ORDER BY d.name_disciplines, t.teachers_name;