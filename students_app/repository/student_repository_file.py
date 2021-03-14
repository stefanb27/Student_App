from repository.student_repository import StudentsRepo
from domain.entities import student
import fileinput
from domain.validators import NoElements
from domain.validators import RepositoryFind


class StudentRepositoryFile(StudentsRepo):
    """

    """
    def __init__(self, fileName):
        # invoke base class __init__ method
        StudentsRepo.__init__(self)
        self.__fileName = fileName
        # load __students from the file
        self.loadFromFile()

    def createStudentFromLine(self, line):
        """
        Process the a line from the file and create a student
        return student
        """
        fields = line.split(' ')
        fields[1] = fields[1][0:-1]
        st = student(fields[0], fields[1])

        return st

    def loadFromFile(self):
        """
          Load __students from file
          process file line by line
        """
        #fh.close()
        '''
        fh = open(self.__fileName, "w")
        for item in lines[:-1]:
            fh.write("%s\n" % item)
        fh.write("%s" % lines[-1])
        fh.close()
        '''
        fh = open(self.__fileName)
        for line in fh:
            if line.strip() == " ":
                continue  # we have an empty line, just skip
            st = self.createStudentFromLine(line)
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
        #fh.write("\n")
        fh.write('%s\n' %line)
        fh.close()




#////////////////////////////////////////////////////////////////////////////

class StudentRepositoryFile2:
    """

    """
    def __init__(self, fileName):
        self.__fileName = fileName

    def __createStudentFromLine(self, line):
        """
        Process the a line from the file and create a student
        return student
        """
        fields = line.split(' ')
        fields[1] = fields[1][0:-1]
        st = student(fields[0], fields[1])

        return st

    def store_student(self, st):
        # invoke store method from the base class
        self.__appendToFile(st)

    def __appendToFile(self, st):
        """
          Append a new line in the file representing the student st
        """
        fh = open(self.__fileName, "a")
        line = st.get_id_student() + " " + st.get_nume_student()
        #fh.write("\n")
        fh.write('%s\n' %line)
        fh.close()

    def update(self):
        with fileinput.FileInput(self.__fileName, inplace = True) as f:
            for line in f:
                print(line, end='')

    def modify_student(self, id_stud, st):
        self.update()
        with fileinput.FileInput(self.__fileName, inplace = True) as f:
            for line in f:
                if id_stud + " " in line :
                    print(st.get_id_student(),st.get_nume_student(), end = '\n')
                else:
                    print(line, end = '')

    def find_student(self, id_s):
        self.update()
        fh = open(self.__fileName)
        ok = 0
        for i, line in enumerate(fh):
            if line.strip() == " ":
                continue  # we have an empty line, just skip
            st = self.__createStudentFromLine(line)
            # invoke the store method from the base class
            if st.get_id_student() == id_s:
                ok = 1
                return st
        fh.close()
        if ok == 0:
            raise RepositoryFind

    def delete_student(self, id_s):
        self.update()
        with fileinput.FileInput(self.__fileName, inplace=True) as f:
            for line in f:
                if self.__createStudentFromLine(line).get_id_student() == id_s:
                    continue
                else:
                    print(line, end='')

    def get_all_students(self):
        self.update()
        rez = []
        fh = open(self.__fileName)
        if fh == ' ':
            raise NoElements
        for line in fh:
            st = self.__createStudentFromLine(line)
            rez.append(st)
        fh.close()
        return rez

    def size(self):
        """
        functie care returneaza numarul de elemente din lista
        """
        self.update()
        cnt = 0
        fh = open(self.__fileName)
        for line in fh:
            cnt += 1
        return cnt

    def get_repo(self):
        self.update()
        dict = {}
        fh = open(self.__fileName)
        for line in fh:
            st = self.__createStudentFromLine(line)
            dict[st.get_id_student()] = st
        return dict











