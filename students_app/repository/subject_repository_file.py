from repository.student_repository import StudentsRepo
from repository.subject_repository import SubjectsRepo
from domain.validators import SubjectValidator
from domain.entities import disciplina
import fileinput


class SubjectRepositoryFile(SubjectsRepo):
    def __init__(self, fileName):
        # invoke base class __init__ method
        SubjectsRepo.__init__(self)
        self.__fileName = fileName
        # load __students from the file
        self.loadFromFile()

    def createSubjectFromLine(self, line):
        """
        Process the a line from the file and create a student
        return student
        """
        fields = line.split(' ')
        fields[2] = fields[2][0: -1]
        sub = disciplina(fields[0], fields[1], fields[2])
        return sub

    def loadFromFile(self):
        """
          Load __students from file
          process file line by line
        """
        fh = open(self.__fileName)
        for line in fh:
            if line.strip() == " ":
                continue  # we have an empty line, just skip
            sub = self.createSubjectFromLine(line)
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
        #fh.write("\n")
        fh.write('%s\n' %line)
        fh.close()



"""
    def modify_subject(self, id_s, new_subj):
        with fileinput.FileInput(self.__fileName, inplace = True) as f:
            for line in f:
                if id_s + " " in line :
                    print(new_subj.get_id_disciplina(),new_subj.get_nume_disciplina(), new_subj.get_profesor(), end = '\n')
                else:
                    print(line, end = '')

    def find_subject(self, id_s):
        fh = open(self.__fileName)
        for i, line in enumerate(fh):
            if line.strip() == " ":
                continue  # we have an empty line, just skip
            sub = self.__createSubjectFromLine(line)
            # invoke the store method from the base class
            if sub.get_id_disciplina() == id_s:
                return sub
        fh.close()

    def delete_subject(self, id_d):
        with fileinput.FileInput(self.__fileName, inplace=True) as f:
            for line in f:
                if self.__createSubjectFromLine(line).get_id_disciplina() == id_d:
                    continue
                else:
                    print(line, end='')

"""