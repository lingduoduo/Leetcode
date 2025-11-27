# Write your MySQL query statement below
SELECT DISTINCT pay_month, department_id, 
(
    CASE
    WHEN avg_dept_sal > avg_company_sal THEN "higher"
    WHEN avg_dept_sal < avg_company_sal THEN "lower"
    WHEN avg_dept_sal = avg_company_sal THEN "same"
    END
) as comparison
FROM 
(
    SELECT s.employee_id, amount, pay_Date, department_id, LEFT(s.pay_date, 7) as pay_month,
     AVG(s.amount) OVER(PARTITION BY s.pay_date) as avg_company_sal,
     AVG(s.amount) OVER(PARTITION BY s.pay_date, e.department_id) as avg_dept_sal
    FROM Salary s
    JOIN Employee e ON s.employee_id = e.employee_id
) as tbl;