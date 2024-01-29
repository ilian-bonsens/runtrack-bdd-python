SELECT * FROM etudiants
WHERE nom = 'Dupuis';

ou 

SELECT *
FROM etudiants
WHERE nom IN (
    SELECT nom
    FROM etudiants
    GROUP BY nom
    HAVING COUNT(*) > 1
    );