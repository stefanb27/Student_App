from domain.entities import disciplina
from domain.tools import is_int
from domain.validators import RepositoryException
from repository.student_repository import StudentsRepo
import string
import random

class SubjectService:
    def __init__(self, rep, val):
        self.__rep = rep
        self.__val = val

    def CreateSubject(self, id_d, nume_d, prof_d):
        '''
        functie care creeaza o disciplina noua in lista de discipline apeland repository-ul
        :param id_d: id-ul disciplinei
        :param nume_d: numele disciplinei
        :param prof_d: profesorul care preda disciplina
        '''
        sub = disciplina(id_d, nume_d, prof_d)
        self.__val.validate(sub)
        self.__rep.store_subject(sub)
        return sub

    def delSubject(self, id_d):
        '''
        fucntie care adauga sterge o disciplina din lista de discipline apeland repository-ul listei
        :param id_d: id-ul disciplinei
        '''
        self.__rep.delete_subject(id_d)

    def modifysubject(self, id_nou, sub_nou):
        '''
        functie care modifica o disciplina dupa id cu alta (un obiect de tip disciplina) apeland repository-ul
        :param id_nou: id-ul studentului
        :param sub_nou: disciplina noua (obiect de tip disciplina)
        '''
        self.__val.validate(sub_nou)
        self.__rep.modify_subject(id_nou, sub_nou)

    def findsubject(self, id_s):
        '''
        functie care cauta o disciplina in lista de discipline dupa id, apeland repository-ul
        :param id_s: id-ul disciplinei
        '''
        if is_int(id_s) == 0:
            raise RepositoryException
        output = self.__rep.find_subject(id_s)
        return output

    def getallsubjects(self):
        '''
        fucntie care afiseaza lista cu tote disicplinele, apeland repository-ul
        '''
        return self.__rep.get_all_subjects()

    def generatesubjects(self, numar):
        i = 1
        while i <= numar:
            try:
                nume = ''.join(random.choices(string.ascii_lowercase, k=7))
                id = ''.join(random.choices(string.digits, k=2))
                prof = ''.join(random.choices(string.ascii_lowercase, k=9))
                self.CreateSubject(id, nume, prof)
                i += 1
            except RepositoryException:
                continue

