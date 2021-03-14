from domain.validators import RepositoryException
from domain.validators import RepositoryFind
from domain.tools import is_int


class SubjectsRepo:
    def __init__(self):
        self.__subjects = {}

    def store_subject(self, sub):
        """
        functie care stocheaza o disciplina in lista de discipline
        :param st: disciplina (obiect de tip disciplina)
        """
        if sub.get_id_disciplina() in self.__subjects:
            raise RepositoryException
        self.__subjects[sub.get_id_disciplina()] = sub

    def delete_subject(self, id_d):
        """
        functie care sterge o disciplina din lista de discipline
        :param id_d: id-ul disciplinei pe care dorim sa o stergem
        """
        if id_d in self.__subjects:
            del self.__subjects[id_d]
        else:
            raise RepositoryException

    def modify_subject(self, id_s, new_subj):
        """
        functie care modifica o disciplina din lista de discipline
        :param id_s: id-ul disciplinei
        :param new_subj: noua disciplina (obiect de tip disciplina)
        """
        if is_int(id_s) == 0:
            raise RepositoryException
        if id_s not in self.__subjects:
            raise RepositoryException
        new_dict = {}
        for key, value in self.__subjects.items():
            if key == id_s:
                new_dict[new_subj.get_id_disciplina()] = new_subj
            else:
                new_dict[key] = value
        self.__subjects = new_dict.copy()

    def find_subject(self, id_s):
        """
        functie care cauta o disciplina in lista de discipline
        :param id_s: id-ul disciplinei
        """
        if id_s in self.__subjects:
            return self.__subjects[id_s]
        else:
            raise RepositoryFind

    def size(self):
        """
        functie care returneaza numarul de discipline din lista
        """
        return len(self.__subjects)

    def get_all_subjects(self):
        """
        functie care returneaza toate disciplinele din lista de discipline
        """
        return list(self.__subjects.values())

    def get_repo(self):
        """
        functie care returneaza repository-ul de discipline
        """
        return dict(self.__subjects)
