from domain.entities import student
from domain.entities import disciplina
from domain.tools import is_nume
from domain.tools import is_int
from domain.entities import Nota

class ValidatorException(Exception):
    def __init__(self, errors):
        self.errors = errors

    def getErrors(self):
        return self.errors


class StudentValidator:

    def validate(self, st):
        """
        functie care valideaza studentul introdus de la tastatura
        :param st: studentul
        """
        errors = []
        if st.get_id_student()=="":
            errors.append("Id-ul nu poate fi ' '")
        if st.get_nume_student()=="":
            errors.append("Numele nu poate fi gol! ")
        if is_int(st.get_id_student()) == 0:
            errors.append("Id-ul trebuie sa fie numeric! ")
        if is_nume(st.get_nume_student()) == 0:
            errors.append("Numele nu poate fi numeric! ")

        if len(errors) > 0:
            raise ValidatorException(errors)

class SubjectValidator:

    def validate(self, sub):
        """
        functie care valideaza disciplina introdusa de la tastatura
        :param sub: disciplina
        """
        errors = []
        if sub.get_id_disciplina() =="":
            errors.append("Id-ul nu poate fi ' '")
        if sub.get_nume_disciplina() =="":
            errors.append("Numele nu poate fi gol! ")
        if sub.get_profesor() =="":
            errors.append("Profesorul nu a fost dat! ")
        if is_int(sub.get_id_disciplina()) == 0:
            errors.append("Id-ul trebuie sa fie numeric! ")
        if is_nume(sub.get_nume_disciplina()) == 0:
            errors.append("Numele nu poate fi numeric! ")
        if is_nume(sub.get_profesor()) == 0:
            errors.append("Numele nu poate fi numeric! ")

        if len(errors) > 0:
            raise ValidatorException(errors)

class NotaValidator:

    def validate(self, n):
        if int(n.get_n()) <= 0 or int(n.get_n())> 10:
            raise ValidatorException("Nota trebuie sa fie intre 0 si 10")

class RepositoryException(Exception):
    pass

class RepositoryFind(Exception):
    pass

class NoElements(Exception):
    pass



