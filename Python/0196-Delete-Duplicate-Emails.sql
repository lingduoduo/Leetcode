###Write your MySQL query statement below
DELETE FROM Person
WHERE Person.Id not in (
    select Person_derived.minId from(
        select min(Id) as minId from Person group by Email
    )Person_derived
)

DELETE p1
FROM Person p1, Person p2
WHERE p1.email = p2.email and p1.id > p2.id