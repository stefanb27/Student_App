from domain.tools import is_int
from domain.entities import Nota
from domain.validators import RepositoryException
from domain.validators import RepositoryFind
from domain.entities import StudentNota
from domain.entities import StudentStats


class StudentsNote:
    def __init__(self, note_rep):
        self.__note_rep = note_rep

    def asignarenota(self, id_stud, id_sub, nota):
        '''
        functie care asigneaza o nota unui student apeland repository-ul
        :param id_stud: id-ul studentului
        :param id_sub: id-ul disciplinei
        :param nota: nota pe care dorim sa o adaugam
        '''
        self.__note_rep.asignare_nota(id_stud, id_sub, nota)

    def updatenote(self):
        '''
        functie care updateaza notele din catalog apeland repository-ul catalogului
        '''
        self.__note_rep.update_note()

    def afisarenote(self):
        '''
        functie care afiseaza notele studentilor din catalog
        '''
        self.__note_rep.afisare_note()

    def listaDupaNume(self, id_d):
        '''
        functie care afiseaza notele si studentii la o disciplina dupa nume (alfabetic)
        :param id_d: id-ul disciplinei
        '''
        if is_int(id_d) == 0:
            raise RepositoryException
        lista = self.__note_rep.lista_dupa_nume(id_d)
        print(lista)


    def listaDupaNote(self, id_d):
        '''
         functie care afiseaza notele si studentii la o disciplina dupa note
        :param id_d: id-ul disciplinei
        '''
        if is_int(id_d) == 0:
            raise RepositoryException
        lista = self.__note_rep.lista_dupa_nota(id_d)
        print(lista)

    def statistici20(self):
        '''
        fucntie care afiseaza lista de studenti dupa media tututor notelor de la toate disciplinele
        '''
        lista = self.__note_rep.statistici_20()
        print(lista)

    def statisticiMaterii(self):
        lista = self.__note_rep.discipline_promovate()
        print(lista)

#/////////////////////////////////////////////////////////////////

class ServNota:
    def __init__(self, lista_note, val_nota, l_s, l_d):
        """
        :param lista_note: lista de obiecte de tip nota (repo)
        val_nota = validator nota
        """
        self.__lista_note = lista_note
        self.__val_nota = val_nota
        self.__l_s = l_s
        self.__l_d = l_d

    def update(self):
        for item in self.__lista_note.getAll():
            if item.get_id_student() not in self.__l_s.get_repo() or item.get_id_sub() not in self.__l_d.get_repo():
                self.__lista_note.del_nota(item.get_id_student(), item.get_id_sub())

    def size(self):
        return self.__lista_note.size()

    def asignare_nota(self, id_stud, id_sub, n):
        #validate nota
        if is_int(id_stud) == 0:
            raise RepositoryException
        if is_int(id_sub) == 0:
            raise RepositoryException
        if id_stud not in self.__l_s.get_repo():
            raise RepositoryFind
        if id_sub not in self.__l_d.get_repo():
            raise RepositoryFind
        self.__l_s.find_student(id_stud) # repo find exc
        grade = Nota(id_stud, id_sub, n)
        self.__val_nota.validate(grade)
        self.__lista_note.asignareNota(grade)

    def afisare_note(self):
        notes = self.__lista_note.getAll()
        catalog = []
        for n in notes:
            l = []
            l.append(self.__l_s.find_student(n.get_id_student()).get_nume_student())
            l.append(self.__l_d.find_subject(n.get_id_sub()).get_nume_disciplina())
            l.append(n.get_n())
            catalog.append(l)
        return catalog

    def lista_dupa_nume(self, id_sub):
        '''
        functie care afiseaza notele si studentii la o disciplina dupa nume (alfabetic)
        :param id_d: id-ul disciplinei
        '''
        notes = self.__lista_note.getAllforSub(id_sub)
        for n in notes:  # n obiect de de tip StudentNota
            st = self.__l_s.find_student(n.get_id_student())
            n.set_nume_stud(st.get_nume_student())

        for n in notes:  # n obiect de de tip StudentNota
            sb = self.__l_d.find_subject(n.get_id_sub())
            n.set_nume_sub(sb.get_nume_disciplina())

        l_final = []
        for key in self.__l_s.get_repo():
            l_note = []
            for i in notes:
                if i.get_id_student() == key:
                    l_note.append(i)
            stats = StudentStats(key, l_note)
            l = []
            l.append(key)
            l.append(self.__l_s.get_repo()[key].get_nume_student())
            l.append(stats.get_medie_disc(id_sub))
            l_final.append(l)

        sorted_l_final = sorted(l_final, key=lambda l_final: l_final[1])
        return sorted_l_final


    def lista_dupa_note(self, id_sub):
        '''
        functie care afiseaza notele si studentii la o disciplina dupa note
        :param id_d: id-ul disciplinei
        '''
        notes = self.__lista_note.getAllforSub(id_sub)
        for n in notes:  # n obiect de de tip StudentNota
            st = self.__l_s.find_student(n.get_id_student())
            n.set_nume_stud(st.get_nume_student())

        for n in notes:  # n obiect de de tip StudentNota
            sb = self.__l_d.find_subject(n.get_id_sub())
            n.set_nume_sub(sb.get_nume_disciplina())

        l_final = []
        for key in self.__l_s.get_repo():
            l_note = []
            for i in notes:
                if i.get_id_student() == key:
                    l_note.append(i)
            stats = StudentStats(key, l_note)
            l = []
            l.append(key)
            l.append(self.__l_s.get_repo()[key].get_nume_student())
            l.append(stats.get_medie_disc(id_sub))
            l_final.append(l)

        sorted_l_final = sorted(l_final, key = lambda l_final : l_final[2], reverse=True)
        return sorted_l_final

    def statistici(self):
        notes = self.__lista_note.getAll()
        l_final = []
        for key in self.__l_s.get_repo():
            l_note = []
            for i in notes:
                if i.get_id_student() == key:
                    l_note.append(i)
            stats = StudentStats(key, l_note)
            l = []
            l.append(key)
            l.append(self.__l_s.get_repo()[key].get_nume_student())
            l.append(stats.get_medie_finala())
            l_final.append(l)
        sorted_l_final = sorted(l_final, key=lambda l_final: l_final[2], reverse=True)
        lungime = len(sorted_l_final)
        sorted_l_final = sorted_l_final[0: -(lungime - (lungime // 5))]
        '''
        l = self.__l_s.get_repo()
        lungime = l // 5
        lista = []
        for i in range(0, lungime):
            lista.append(sorted_l_final[i])
        return lista
        '''
        return sorted_l_final

    def stats(self):
        '''
        fucntie care afiseaza lista de studenti dupa media tututor notelor de la toate disciplinele
        '''
        lista_materii = []
        for key, value in self.__l_s.get_repo().items():
            l = self.__lista_note.getAllforStud(key)
            ok1 = 0
            ok2 = 0
            for item in l:
                if int(item.get_n()) < 5:
                    ok1 = 1
                if int(item.get_n()) > 7:
                    ok2 = 1
            if ok1 == 1 and ok2 == 1:
                lista = []
                lista.append(value.get_id_student())
                lista.append(value.get_nume_student())
                lista_materii.append(lista)
        return lista_materii






