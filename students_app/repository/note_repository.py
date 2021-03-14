from domain.validators import RepositoryException
from domain.validators import RepositoryFind
from domain.tools import is_int
from domain.entities import StudentNota

class NoteRep:
    def __init__(self, l_s, l_d):
        self.__note = {}
        self.__l_s = l_s
        self.__l_d = l_d

    def asignare_nota(self, id_stud, id_sub, nota):
        """
        functie care asigneaza o nota unui student
        :param id_stud: id-ul studentului
        :param id_sub: id-ul disciplinei
        :param nota: nota pe care dorim sa o asignam
        """
        if is_int(id_stud) == 0:
            raise RepositoryException
        if is_int(id_sub) == 0:
            raise RepositoryException
        if id_stud not in self.__l_s.get_repo():
            raise RepositoryFind
        elif id_sub not in self.__l_d.get_repo():
            raise RepositoryFind
        else:
            self.__note[id_stud][id_sub].append(nota)

    def update_note(self):
        """
        functie care updateaza catalgoul de note
        """
        for key1, value1 in self.__l_s.get_repo().items():
            if key1 not in self.__note:
                self.__note[key1] = {}
            elif key1 in self.__note and key1 not in self.__l_s.get_repo():
                del self.__note[key1]
            for key2, value2 in self.__l_d.get_repo().items():
                if key2 not in self.__note[key1]:
                    self.__note[key1][key2] = []
                elif key2 in self.__note[key1] and key2 not in self.__l_d.get_repo():
                    del self.__note[key1][key2]

    def afisare_note(self):
        """
        functie care afiseaza notele tuturor studentilor
        """
        print("-----------------CATALOG---------------------")
        if len(self.get_repo()) == 0:
            print("Nu exista date momentan ")
        else:
            for k, v in self.__note.items():
                if k not in self.__l_s.get_repo():
                    continue
                if len(self.__l_d.get_repo()) != 0:
                    print(self.__l_s.get_repo()[k].get_nume_student(), '--------------------------------')
                else:
                    print(self.__l_s.get_repo()[k].get_nume_student())
                for i, j in v.items():
                    if i not in self.__l_d.get_repo():
                        continue
                    print(self.__l_d.get_repo()[i].get_nume_disciplina(), j)
                print('------------------------------------------')

    def lista_dupa_nume(self, id_d):
        """
        functie care afiseaza lista la o discplina de studenti si note dupa nume
        :param id_d: id-ul discipline
        """
        if id_d not in self.__l_d.get_repo():
            raise RepositoryFind
        lista = []
        for key, value in self.__note.items():
            l = []
            l.append(key)
            l.append(self.__l_s.get_repo()[key].get_nume_student())
            l.append(self.__note[key][id_d])
            lista.append(l)
        lista.sort(key=lambda x: x[1])
        return lista

    def lista_dupa_nota(self, id_d):
        """
        functie care afiseaza lista la o disciplina de studeti si de note dupa note
        :param id_d: id-ul disciplinei
        """
        if id_d not in self.__l_d.get_repo():
            raise RepositoryFind
        lista = []
        for key, value in self.__note.items():
            ls = []
            ls.append(key)
            ls.append(self.__l_s.get_repo()[key].get_nume_student())
            ls.append(self.__note[key][id_d])
            cnt = 0
            suma = 0
            for l in range(0, len(value[id_d])):
                suma = suma + int(value[id_d][l])
                cnt += 1
            if suma != 0:
                medie = round((suma / cnt), 2)
                ls.append(medie)
            else:
                ls.append(0)
            lista.append(ls)
        lista.sort(key=lambda x: x[3])
        lista.reverse()
        return lista

    def discipline_promovate(self):
        lista_materii = []
        for key in self.__l_d.get_repo():
            l = self.lista_dupa_nota(key)
            count = 0
            for i in range(0, len(l)):
                if l[i][3] > 5:
                    count += 1
            if count >= self.__l_s.size():
                d = self.__l_d.get_repo()[key]
                m = []
                m.append(d.get_id_disciplina())
                m.append(d.get_nume_disciplina())
                lista_materii.append(m)
        return lista_materii

    def statistici_20(self):
        """
        functie care afiseaza primii 20% din studenti dupa media notelor la toate disciplinele
        """
        if len(self.__note) < 5:
            print("Nu exista studenti suficienti pentru a crea statistica!")
        else:
            lista = []
            for key, value in self.__note.items():
                ls = []
                ls.append(key)
                ls.append(self.__l_s.get_repo()[key].get_nume_student())
                cnt = 0
                suma = 0
                for i in value.values():
                    for l in range(0, len(i)):
                        suma = suma + int(i[l])
                        cnt += 1
                if suma != 0:
                    medie = round((suma / cnt), 2)
                    ls.append(medie)
                lista.append(ls)
            lista.sort(key=lambda x: x[2])
            lista.reverse()
            l_final = []
            for i in range(0, (len(self.__note) // 5)):
                l_final.append(lista[i])
            return l_final

    def get_repo(self):
        return dict(self.__note)

#//////////////////////////////////////////////////////////////////////////////



class NoteRepo:
    def __init__(self):
        self.__lista_note = []

    def asignareNota(self, n):
        """
        functie care asigneaza o nota unui student si adauga obiectul de tip nota (n) in lista de note
        :param n: n obiect de tip nota
        """
        self.__lista_note.append(n)

    def size(self):
        """
        functie care returneaza numarul de note din catalog
        """
        return len(self.__lista_note)

    def del_nota(self, id_stud, id_sub):
        for item in self.__lista_note:
            if item.get_id_student() == id_stud and item.get_id_disciplina() == id_sub:
                self.__lista_note.remove(item)

    def find(self, id_stud, id_sub):
        """
        functie care cauta o nota pt id-ul sau si al disciplinei dat
        :param id_stud: id-ul studentului
        :param id_sub: id-ul materie
        """
        for n in self.__lista_note:
            if n.get_id_student() == id_stud and n.get_id_disciplina() == id_sub:
                return n
        return None

    def getAllforStud(self, id_stud):
        """
        functie care returneaza lista de note a unui student
        :param id_stud: id-ul studentului
        """
        note = []
        for n in self.__lista_note:
            if n.get_id_student() == id_stud:
                note.append(n)
        return note

    def getAllforSub(self, id_sub):
        """
        functie care returneaza lista cu toate notele la o disciplina data
        :param id_sub: id-ul disciplinei
        """
        note = []
        for n in self.__lista_note:
            if n.get_id_disciplina() == id_sub:
                sn = StudentNota(n.get_id_student(), id_sub, n.get_n())
                note.append(sn)
        return note

    def getAll(self):
        """
        functie care returneaza toate notele studentilor
        """
        note = []
        for n in self.__lista_note:
            sn = StudentNota(n.get_id_student(), n.get_id_disciplina(), n.get_n())
            note.append(sn)
        return note






