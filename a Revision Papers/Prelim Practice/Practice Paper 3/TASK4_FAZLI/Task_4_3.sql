SELECT Student.Class, Student.IndexNo, Student.Name,
Test.TestID, Result.score, Test.MaxScore

FROM Student, Test, Result

WHERE Student.Class = '19J08' AND
Test.Subject = 'Economics' AND
Test.TestID = Result.TestID AND
Student.MatricNo = Result.MatricNo

ORDER BY Test.TestID, Student.IndexNo ASC