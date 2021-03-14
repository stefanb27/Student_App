from repository.student_repository import StudentsRepo
from repository.subject_repository import SubjectsRepo
from domain.validators import ValidatorException
from domain.validators import SubjectValidator
from domain.entities import student
from domain.entities import disciplina

class StudentRepositoryFile(StudentsRepo):
    """

    """

    def __init__(self, fileName):
        # invoke base class __init__ method
        StudentsRepo.__init__(self)
        self.__fileName = fileName
        # load __students from the file
        self.__loadFromFile()

    def __createStudentFromLine(self, line):
        """
        Process the a line from the file and create a student
        return student
        """
        fields = line.split(' ')
        st = student(fields[0], fields[1])
        return st

    def __loadFromFile(self):
        """
          Load __students from file
          process file line by line
        """
        fh = open(self.__fileName)
        for line in fh:
            if line.strip() == " ":
                continue  # we have an empty line, just skip
            st = self.__createStudentFromLine(line)
            # invoke the store method from the base class
            StudentsRepo.store_student(self, st)
        fh.close()

    def store_student(self, st):
        # invoke store method from the base class
        StudentsRepo.store_student(self, st)
        self.__appendToFile(st)

    def __appendToFile(self, st):
        """
          Append a new line in the file representing the student st
        """
        fh = open(self.__fileName, "a")
        line = st.get_id_student() + " " + st.get_nume_student()
        fh.write("\n")
        fh.write(line)
        fh.close()

'''
def testRepo():
    fileName = "test.txt"
    # make sure wi start with an empty file
    clearFileContent(fileName)
    repo = StudentRepositoryFile(fileName)
    assert repo.size() == 0
    repo.store(Student("9", "Ion2", "Adr2"))
    assert repo.size() == 1


def testRead():
    fileName = "c:/temp/test.txt"
    # make sure wi start with an empty file
    clearFileContent(fileName)

    repo = StudentRepositoryFile(fileName)
    repo.store(Student("8", "Ion1", "Adr1"))
    repo.store(Student("9", "Ion2", "Adr2"))

    repo2 = StudentRepositoryFile(fileName)
    assert repo2.size() == 2


testRepo()
testRead()

'''

class SubjectRepositoryFile(SubjectsRepo):
    def __init__(self, fileName):
        # invoke base class __init__ method
        SubjectsRepo.__init__(self)
        self.__fileName = fileName
        # load __students from the file
        self.__loadFromFile()

    def __createSubjectFromLine(self, line):
        """
        Process the a line from the file and create a student
        return student
        """
        fields = line.split(' ')
        sub = disciplina(fields[0], fields[1], fields[2])
        return sub



    def __loadFromFile(self):
        """
          Load __students from file
          process file line by line
        """
        fh = open(self.__fileName)
        for line in fh:
            if line.strip() == " ":
                continue  # we have an empty line, just skip
            sub = self.__createSubjectFromLine(line)
            # invoke the store method from the base class
            SubjectsRepo.store_subject(self, sub)
        fh.close()

    def store_subject(self, sub):
        # invoke store method from the base class
        val = SubjectValidator()
        val.validate(sub)
        SubjectsRepo.store_subject(self, sub)
        self.__appendToFile(sub)

    def __appendToFile(self, sub):
        """
          Append a new line in the file representing the student st
        """
        fh = open(self.__fileName, "a")
        line = sub.get_id_disciplina() + " " + sub.get_nume_disciplina() + " " + sub.get_profesor()
        fh.write("\n")
        fh.write(line)
        fh.close()
