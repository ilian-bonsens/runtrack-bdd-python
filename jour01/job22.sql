select * from etudiants
where age = (
    select min(age) from etudiants
    );