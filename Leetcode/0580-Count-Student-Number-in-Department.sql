SELECT d.department_name, count(s.student_id) as student_number
FROM department d 
RIGHT JOIN student s
ON d.department_id = s.department_id
GROUP BY d.department_name
ORDER BY student_number DESC, d.department_name