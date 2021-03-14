from repository.student_repository_file import StudentRepositoryFile2
from repository.student_repository_file import StudentRepositoryFile
from repository.subject_repository_file import SubjectRepositoryFile
from domain.tools import read_command
from domain.entities import student
from domain.entities import disciplina
from domain.validators import ValidatorException
from domain.validators import RepositoryException
from domain.validators import RepositoryFind
from services.student_serv import StudentService
from services.note_serv import ServNota
from services.subject_serv import SubjectService
from repository.student_repository import StudentsRepo
from repository.subject_repository import SubjectsRepo
from domain.validators import StudentValidator
from domain.validators import SubjectValidator
from domain.validators import NotaValidator
from repository.note_repository import NoteRepo
from repository.note_repository_file import NoteRepoFile
from domain.validators import NoElements

def menu():
    print('--------------------------------------MENIU-------------------------------------')
    print('1. Adaugati student in lista de studenti')
    print('2. Afisati lista de studenti')
    print('3. Adaugati disciplina in lista de discipline')
    print('4. Afisati lista de discipline')
    print('5. Sterge student din lista de studenti')
    print('6. Sterge disciplina din lista de discipline')
    print('7. Modifica student din lista de studenti')
    print('8. Modifica disciplina din lista de discipline')
    print('9. Cauta student din lista de studenti (id_student)')
    print('10. Cauta disciplina din lista de discipline (id disciplina)')
    print('11. Asigneaza o nota unui student')
    print('12. Afisati catalogul cu note')
    print('13. Afisati studentii si notele la o materie dupa nume')
    print('14. Afisati studentii si notele la o materie dupa note')
    print('15. Afiseaza primii 20% studenti dupa notele la toate disciplinele')
    print('16. Genereaza un numar de studenti')
    print('17. Afiseaza studentii care au cel putin o nota sub 5 si una peste 7')
    print('--------------------------------------MENIU-------------------------------------')

class Console:
    def __init__(self, st, sb, cat):
        self.__st = st
        self.__sb = sb
        self.__cat = cat

    def __showAllStudents(self):
        """
        functie care afiseaza toti studentii
        """
        students = self.__st.getallstudents()
        if len(students) == 0:
            print("Nu exista studenti in catalog!")
        else:
             print('Id    Nume')
             for s in students:
                 #print(s)
                 print(s.get_id_student(),' '*(4 - len(s.get_id_student())), s.get_nume_student())

    def __showAllStudentsFile(self):
        try:
            self.__st.getallstudents()
        except NoElements:
            print("Nu exista elemente! ")


    def __addStudent(self):
        """
        functie care adauga un student in lista de studenti
        """
        id_s = input("Dati id-ul studentului: ")
        nume_s = input("Dati numele studentului: ")

        #aici bag cu try exceptiile
        try:
            stud = self.__st.createStudent(id_s, nume_s)
            #print(stud.get_id_student(), stud.get_nume_student())
            print("Student " + stud.get_nume_student() + " saved..")
        except RepositoryException:
            print("Exista deja acest id")
        except ValidatorException as ex:
            print(ex.getErrors())

    def __addSubject(self):
        """
        functie care adauga o disciplina in lista de discipline
        """
        id_d = input("Dati id-ul disciplinei: ")
        nume_d = input("Dati numele disciplinei: ")
        prof_d = input("Dati profesorul: ")
        try:
            sub = self.__sb.CreateSubject(id_d, nume_d, prof_d)
            print("Disciplina " + sub.get_nume_disciplina() + " saved..")
        except ValidatorException as sx:
            print(sx.getErrors())
        except RepositoryException:
            print("Exista deja acest id")

    def __showAllSubjects(self):
        """
        functie care afiseaza toate disciplinele
        """
        subjects = self.__sb.getallsubjects()
        if len(subjects) == 0:
            print("Nu exista discipline in catalog!")
        else:
            print('Id    Nume        Profesor')
            for s in subjects:
                #print(s)
                print(s.get_id_disciplina(), '   ',s.get_nume_disciplina(),' '*(10 - len(s.get_nume_disciplina())) ,s.get_profesor())

    def __deleteStudent(self):
        """
        functie care sterge un student din lista de studenti
        """
        id_s = input("Dati id-ul studentului: ")
        try:
            self.__st.delStudent(id_s)
        except RepositoryException:
            print("Nu exista acest id in lista de studenti! ")

    def __deleteSubject(self):
        """
        functie care sterge o disciplina din lista de discipline
        """
        id_d = input("Dati id-ul disciplinei: ")
        try:
            self.__sb.delSubject(id_d)
        except RepositoryException:
            print("Nu exista acest id in lista de discipline!")

    def __modifyStudent(self):
        """
        functie care modifica un student din lista de studenti
        """
        id_s = input("Dati id-ul studentului pe care doriti sa il modificati: ")
        nume_s_nou = input("Dati numele noului student: ")
        stud = student(id_s, nume_s_nou)
        try:
            self.__st.modifystudent(id_s, stud)
        except RepositoryException:
            print("Id invalid! ")
        except ValidatorException as er:
            print(er.getErrors())

    def __modifySubject(self):
        """
        functie care modifica o disciplina din lista de discipline
        """
        id_s = input("Dati id-ul disciplinei pe care doriti sa o inlocuiti: ")
        nume_s_nou = input("Dati numele disciplinei noi: ")
        nume_p_nou = input("Dati numele noului profesor: ")
        subj = disciplina(id_s, nume_s_nou, nume_p_nou)
        try:
            self.__sb.modifysubject(id_s, subj)
        except RepositoryException:
            print("Id invalid!")
        except ValidatorException as ex:
            print(ex.getErrors())
    def __findStudent(self):
        """
        functie care cauta un student in lista de studenti
        """
        id_s = input("Dati id-ul studentului: ")
        try:
            st = self.__st.findstudent(id_s)
            print(st.get_id_student(), st.get_nume_student())
        except RepositoryException:
            print("Id invalid!")
        except RepositoryFind:
            print("Nu exista student cu acest id!")

    def __findSubject(self):
        """
        functie care cauta o disciplina in lista de discipline
        """
        id_s = input("Dati id-ul disciplinei: ")
        try:
            self.__sb.findsubject(id_s)
        except RepositoryException:
            print("Id invalid!")
        except RepositoryFind:
            print("Nu exista disciplina cu acest id!")

    def __asignareNota(self):
        """
        functie care asigneaza o nota unui student
        """
        id_stud = input("Dati id-ul studentului: ")
        id_sub = input("Dati id-ul disciplinei: ")
        nota = input("Dati nota: ")
        try:
            self.__cat.asignare_nota(id_stud, id_sub, nota)
        except RepositoryFind:
            print("Nu exista acest id!")
        except RepositoryException:
            print("Id invaldi!")


    def __afisareNote(self):
        """
        functie care afiseaza toti studentii si toate notele fiecaruia
        """
        catalog = self.__cat.afisare_note()
        for i in range(0,len(catalog)):
            print(catalog[i])

    def __afisareNoteFile(self):
        pass

    def __ListaDupaNume(self):
        """
        functie care afiseaza lista de studenti si notele de la o disciplina dupa nume
        """
        try:
            id_d = input("Dati id-ul disciplinei: ")
            l = self.__cat.lista_dupa_nume(id_d)
            for i in l:
                print(i)
        except RepositoryException:
            print("Id invalid!")
        except RepositoryFind:
            print("Nu exista acest id!")

    def __ListaDupaNote(self):
        """
        functie care afiseaza lista de studenti si notele de la o disciplina dupa note
        """
        try:
            id_d = input("Dati id-ul disciplinei: ")
            l = self.__cat.lista_dupa_note(id_d)
            for i in l:
                print(i)
        except RepositoryException:
            print("Id invalid!")
        except RepositoryFind:
            print("Nu exista acest id!")

    def __Statistici20(self):
        """
        functie care afiseaza primii 20% studenti de la toate materiile
        """
        l = self.__cat.statistici()
        for i in l:
            print(i)
    def __gen_stud(self):
        """
        functie care genereaza un nr de studenti
        """
        nr = int(input("Dati numarul: "))
        self.__st.generatestudents(nr)

    def __Statistici(self):
        """
        functie care afiseaza materiile la care cel putin jumatate din studenti au promovat
        """
        l = self.__cat.stats()
        for i in l:
            print(i)


    def showUI(self):
        while True:
            menu()
            cmd = read_command("Dati comanda: ")
            if cmd == '1':
                self.__addStudent()
            if cmd == '2':
                self.__showAllStudents()
            if cmd == '3':
                self.__addSubject()
            if cmd == '4':
                self.__showAllSubjects()
            if cmd == '5':
                self.__deleteStudent()
            if cmd == '6':
                self.__deleteSubject()
            if cmd == '7':
                self.__modifyStudent()
            if cmd == '8':
                self.__modifySubject()
            if cmd == '9':
                self.__findStudent()
            if cmd == '10':
                self.__findSubject()
            if cmd == '11':
                self.__asignareNota()
            if cmd == '12':
                self.__afisareNote()
            if cmd == '13':
                self.__ListaDupaNume()
            if cmd == '14':
                self.__ListaDupaNote()
            if cmd == '15':
                self.__Statistici20()
            if cmd == '16':
                self.__gen_stud()
            if cmd == '17':
                self.__Statistici()

rep_stud = StudentRepositoryFile2('students_file')
rep_sub = SubjectRepositoryFile('subjects_file')
#rep_stud = StudentsRepo()
#rep_sub = SubjectsRepo()
#rep_note = NoteRepo()
rep_note = NoteRepoFile('note_file')
val_stud = StudentValidator()
val_sub = SubjectValidator()
val_nota = NotaValidator()
note = ServNota(rep_note, val_nota, rep_stud,rep_sub)
stud = StudentService(rep_stud, val_stud)
sub = SubjectService(rep_sub, val_sub)
ui = Console(stud, sub, note)
ui.showUI()

