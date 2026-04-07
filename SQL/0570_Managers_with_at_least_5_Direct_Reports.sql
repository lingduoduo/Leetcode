with tbl as (
    SELECT managerId
	FROM Employee
	GROUP BY 1
	HAVING count(*) >= 5
)

select e.name
from Employee e
inner join tbl
on e.id = tbl.managerId