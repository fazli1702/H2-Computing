SELECT Student.Class, Student.IndexNo 
FROM Student, Candidate, Vote 
WHERE Candidate.Name = 'Ee Pei Chi Neoma'
AND Candidate.CandidateNo = Vote.CandidateNo
AND Student.MatricNo = Vote.MatricNo
ORDER BY Student.Class ASC, Student.IndexNo ASC