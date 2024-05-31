UPDATE Grade
inner join Assignments on Grade.disciplines_id = Assignments.discipline_id and Grade.student_id = Assignments.student_id
set Grade.grade=(select sum(Assignments.grade) from  Assignments where  Assignments.discipline_id = Grade.disciplines_id and Assignments.student_id = Grade.student_id)