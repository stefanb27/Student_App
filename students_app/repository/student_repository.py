from domain.validators import RepositoryException
from domain.validators import RepositoryFind
from domain.tools import is_int


class StudentsRepo:
    def __init__(self):
        self.__students = {}

    def store_student(self, st):
        """
        functie care stocheaza un student in lista
        :param st: studentul (obiect de tip student)
        """
        if st.get_id_student() in self.__students:
            raise RepositoryException
        self.__students[st.get_id_student()] = st

    def size(self):
        """
        functie care returneaza numarul de elemente din lista
        """
        return len(self.__students)

    def delete_student(self, id_s):
        """
        functie care sterge un student din lista de studenti
        :param id_s: id-ul studentului
        """
        if id_s in self.__students:
            del self.__students[id_s]
        else:
            raise RepositoryException

    def modify_student(self, id_s, new_stud):
        """
        functie care modifica numele unui student
        :param id_s: id-ul studentului
        :param new_stud: noul student (obiect de tip student)
        """
        if is_int(id_s) == 0:
            raise RepositoryException
        if id_s not in self.__students:
            raise RepositoryException
        #if new_stud.get_id_student() in self.__students:
            #raise RepositoryException
        new_dict = {}
        for key, value in self.__students.items():
            if key == id_s:
                new_dict[new_stud.get_id_student()] = new_stud
            else:
                new_dict[key] = value
        self.__students = new_dict.copy()

    def find_student(self, id_s):
        """
        functie care cauta un student in lista dupa id
        :param id_s: id-ul studentului
        """
        if id_s in self.__students:
            return self.__students[id_s]
        else:
            raise RepositoryFind


    def get_all_students(self):
        """
        functie care returneaza lista de studenti
        """
        return list(self.__students.values())

    def get_repo(self):
        """
        functie care returneaza repository-ul
        """
        return dict(self.__students)



