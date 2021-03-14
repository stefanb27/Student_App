from domain.entities import student
from domain.validators import RepositoryException
from domain.tools import is_int

import string
import random

class StudentService:
    def __init__(self, rep, val):
        self.__rep = rep
        self.__val = val

    def createStudent(self, id_st, nume_st):
        '''
        functie care adauga un student in lista de studenti apeland repository-ul
        :param1 id_st: id-ul studentului
        :param2 nume_st: numele studentului
        '''
        st = student(id_st, nume_st)
        self.__val.validate(st)
        self.__rep.store_student(st)
        return st

    def delStudent(self, id_s):
        '''
        functie care sterge un student din lista de studenti apeland repository-ul si valodatorul pentru a verifica
        :param id_s: id-ul studentului
        '''
        self.__rep.delete_student(id_s)

    def modifystudent(self, id_s, new_stud):
        '''
        functie care modifica un student cu altul prin apelarea repository-ului si a validatorului pt validarea datelor
        :param id_s: id-ul studentului pt a fi identificat cel pe care vrem sa il modificam
        :param new_stud: noul student, obiect de tip student
        '''
        self.__val.validate(new_stud)
        self.__rep.modify_student(id_s, new_stud)

    def findstudent(self, id_s):
        '''
        functie care cauta un student in lista de studenti dupa id apeland repository-ul
        :param id_s: id-ul studentului
        '''
        if is_int(id_s) == 0:
            raise RepositoryException
        output = self.__rep.find_student(id_s)
        return output

    def getallstudents(self):
        '''
        functie care returneaza lista cu toti studentii
        '''
        return self.__rep.get_all_students()

    def generatestudents(self, numar):
        i = 1
        while i <= numar:
            try:
                nume = ''.join(random.choices(string.ascii_lowercase, k=7))
                id = ''.join(random.choices(string.digits, k=2))
                self.createStudent(id, nume)
                i += 1
            except RepositoryException:
                continue





