###Write your MySQL query statement below
DELETE FROM Person
WHERE Person.Id not in (
    select Person_derived.minId from(
        select min(Id) as minId from Person group by Email
    )Person_derived
)
