

class student:
    def __init__(self, id_student, nume_student):
        self.__id_student = id_student
        self.__nume_student = nume_student

    def get_id_student(self):
        '''
        functie de tip getter care returneaza id-ul studentului
        '''
        return self.__id_student

    def get_nume_student(self):
        '''
        functie de tip getter care returneaza numele studentului
        '''
        return self.__nume_student

    def set_nume_student(self, Nume):
        '''
        functie de tip setter care seteaza numele unui student
        :param Nume: numele studentului pe care il dorim
        '''
        self.__nume_student = Nume

    def set_id_student(self, Id):
        '''
        functie de tip setter care seteaza id-ul unui student
        :param Id: id-ul studentului pe care il dorim
        '''
        self.__id_student = Id

    def __eq__(self, other):
        return self.get_id_student() == other.get_id_student()



class disciplina:
    def __init__(self, id_disciplina, nume_disciplina, profesor):
        self.__id_disciplina = id_disciplina
        self.__nume_disciplina = nume_disciplina
        self.__profesor = profesor

    def get_id_disciplina(self):
        '''
        functie de tip getter care returneaza id-ul disciplinei
        '''
        return self.__id_disciplina

    def get_nume_disciplina(self):
        '''
        functie de tip getter care returneaza numele disciplinei
        '''
        return self.__nume_disciplina

    def get_profesor(self):
        '''
        functie de tip getter care returneaza numele profesorului
        '''
        return self.__profesor

    def set_nume_disciplina(self, Nume):
        '''
        functie de tip setter care seteaza numele disciplinei
        '''
        self.__nume_disciplina = Nume

    def set_id_disciplina(self, Id):
        '''
        functie de tip setter care seteaza id-ul disciplinei
        '''
        self.__id_disciplina = Id

    def set_profesor(self, p):
        '''
        functie de tip setter care seteaza numele profesorului
        '''
        self.__profesor = p

    def __eq__(self, other):
        return self.get_id_disciplina() == other.get_id_disciplina()

class Nota:
    def __init__(self, id_student, id_disciplina, nota):
        self.__id_student = id_student
        self.__id_disciplina = id_disciplina
        self.__nota = nota

    def get_id_student(self):
        return self.__id_student

    def get_id_disciplina(self):
        return self.__id_disciplina

    def get_n(self):
        return self.__nota

class StudentNota:
    """
    DTO
    """
    def __init__(self, id_stud, id_sub, nota):
        self.__id_stud = id_stud
        self.__id_sub = id_sub
        self.__nota = nota
        self.__nume_stud = None
        self.__nume_sub = None

    def get_id_student(self):
        return self.__id_stud

    def get_n(self):
        return self.__nota

    def get_id_sub(self):
        return self.__id_sub

    def get_nume_student(self):
        return self.__nume_stud

    def get_nume_disciplina(self):
        return  self.__nume_sub

    def set_nume_stud(self, n):
        self.__nume_stud = n

    def set_nume_sub(self, n):
        self.__nume_sub = n

class StudentStats:
    """
    DTO
    """
    def __init__(self, id_stud, note): #note e lista notelor de la studentul respectiv
        self.__id_stud = id_stud
        self.__note = note
        self.__cat = {}
        #self.__medie_all = []
        self.update()
        self.set_note()
        #self.print_note()

    def update(self):
        for i in self.__note:
            if i.get_id_sub() not in self.__cat:
                self.__cat[i.get_id_sub()] = []

    #def print_note(self):
       #for key in self.__cat:
            #print(key, self.__cat[key])

    def get_medie_disc(self, id_sub):
        l = self.get_note_disc(id_sub)
        sum = 0
        for i in range(0, len(l)):
            sum = sum + int(l[i])
        medie = round((sum / len(l)), 2)
        return medie

    def get_medie_finala(self):
        medie = 0
        for key in self.__cat:
            m = self.get_medie_disc(key)
            medie += m
        #if self.get_size() != 0:
        medie_finala = round((medie / self.get_size()), 2)
        #print(medie_finala)
        return medie_finala

    def get_note_disc(self, id_sub):
        return self.__cat[id_sub]

    def set_note(self):
        for i in self.__note:
            self.__cat[i.get_id_sub()].append(i.get_n())

    def get_size(self):
        #print(len(self.__cat))
        return len(self.__cat)


