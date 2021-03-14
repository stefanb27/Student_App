import domain.tools as t
from domain.entities import student
from domain.entities import disciplina
from domain.entities import Nota
from domain.entities import StudentNota
from domain.entities import StudentStats
from repository.student_repository import StudentsRepo
from repository.subject_repository import SubjectsRepo
from repository.memory_file import StudentRepositoryFile
from repository.memory_file import SubjectRepositoryFile
from repository.note_repository import NoteRep
from services.student_serv import StudentService
from services.subject_serv import SubjectService
from services.note_serv import StudentsNote
from domain.validators import RepositoryException
from domain.validators import RepositoryFind
from domain.validators import ValidatorException
from domain.validators import StudentValidator
from domain.validators import SubjectValidator
from repository.note_repository import NoteRepo
from services.note_serv import ServNota
from domain.validators import NotaValidator
import unittest
from repository.student_repository_file import StudentRepositoryFile2
from repository.student_repository_file import StudentRepositoryFile
from repository.subject_repository_file import SubjectRepositoryFile
from repository.note_repository_file import NoteRepoFile
import os

class testEntities(unittest.TestCase):

    def setUp(self):
        self.stud = student('1', 'gigel')
        self.sub = disciplina('1', 'mate', 'pop')

    def test_get_id_student(self):
        self.assertEqual(self.stud.get_id_student(), '1')
    def test_get_nume_student(self):
        self.assertEqual(self.stud.get_nume_student(), 'gigel')
    def test_set_id_student(self):
        self.stud.set_id_student('2')
        self.assertEqual(self.stud.get_id_student(), '2')
    def test_set_nume_student(self):
        self.stud.set_nume_student('gicu')
        self.assertEqual(self.stud.get_nume_student(), 'gicu')
    def test_eq_student(self):
        self.stud2 = student('1', 'gigel')
        self.assertEqual(self.stud.__eq__(self.stud2), 1)
    def test_get_id_discipline(self):
        self.assertEqual(self.sub.get_id_disciplina(), '1')
    def test_get_nume_disciplina(self):
        self.assertEqual(self.sub.get_nume_disciplina(), 'mate')
    def test_get_profesor(self):
        self.assertEqual(self.sub.get_profesor(), 'pop')
    def test_set_it_discipline(self):
        self.sub.set_id_disciplina('2')
        self.assertEqual(self.sub.get_id_disciplina(), '2')
    def test_set_nume_disicpline(self):
        self.sub.set_nume_disciplina('info')
        self.assertEqual(self.sub.get_nume_disciplina(), 'info')
    def test_set_profesor(self):
        self.sub.set_profesor('nicu')
        self.assertEqual(self.sub.get_profesor(), 'nicu')
    def test_eq_disicpline(self):
        self.sub2 = disciplina('1', 'mate', 'pop')
        self.assertEqual(self.sub.__eq__(self.sub2), 1)

class testEntitiesNota(unittest.TestCase):
    def setUp(self):
        self.nota = Nota('1', '2', 10)
        self.grade = StudentNota('1', '3', 9)
        self.grade.__nume_stud = 'gicu'
        self.grade.__nume_sub = 'mate'

    def test_get_id_student(self):
        self.assertEqual(self.nota.get_id_student(), '1')
    def test_get_id_disiciplinea(self):
        self.assertEqual(self.nota.get_id_disciplina(), '2')
    def test_get_n(self):
        self.assertEqual(self.nota.get_n(), 10)
    def test_get_id_stud(self):
        self.assertEqual(self.grade.get_id_student(), '1')
    def test_get_id_sub(self):
        self.assertEqual(self.grade.get_id_sub(), '3')
    def test_get_nota(self):
        self.assertEqual(self.grade.get_n(), 9)
    def test_set_nume_student(self):
        self.grade.set_nume_stud('gicu')
        self.assertEqual(self.grade.get_nume_student(), 'gicu')
    def test_get_nume_student(self):
        self.grade.set_nume_stud('nicu')
        self.assertEqual(self.grade.get_nume_student(), 'nicu')
    def test_set_nume_disciplina(self):
        self.grade.set_nume_sub('mate')
        self.assertEqual(self.grade.get_nume_disciplina(), 'mate')
    def test_get_nume_disciplina(self):
        self.grade.set_nume_sub('info')
        self.assertEqual(self.grade.get_nume_disciplina(), 'info')

class testStudentStats(unittest.TestCase):
    def setUp(self):
        self.l_note = []
        self.nota1 = StudentNota('1', '2', 10)
        self.nota2 = StudentNota('1', '1', 9)
        self.nota3 = StudentNota('1', '2', 7)
        self.l_note.append(self.nota1)
        self.l_note.append(self.nota2)
        self.l_note.append(self.nota3)
        self.studstats = StudentStats('1', self.l_note)

    def test_update(self):
        self.nota4 = StudentNota('1', '3', 10)
        self.l_note.append(self.nota4)
        self.studstats.update()
        self.assertEqual(self.studstats.get_size(), 3)
    def test_medie_disc(self):
        self.assertEqual(self.studstats.get_medie_disc('2'), 8.5)
    def test_medie_finala(self):
        self.assertEqual(self.studstats.get_medie_finala(), 8.75)
    def test_get_size(self):
        self.assertEqual(self.studstats.get_size(), 2)



class testStudentService(unittest.TestCase):
    def setUp(self):
        self.repo = StudentsRepo()
        self.val = StudentValidator()
        self.serv = StudentService(self.repo, self.val)
        self.serv.createStudent('1', 'ana')
        self.serv.createStudent('2', 'florin')
        self.serv.createStudent('3', 'marian')

    def test_add(self):
        self.serv.createStudent('4', 'dorin')
        self.assertEqual(self.repo.size(), 4)

        with self.assertRaises(ValidatorException):
            self.serv.createStudent('1', '2')

        self.serv.createStudent('5', 'giani')
        self.assertEqual(self.repo.size(), 5)

        with self.assertRaises(ValidatorException):
            self.serv.createStudent('ana', 'ana')

        self.serv.createStudent('6', 'doru')
        self.assertEqual(self.repo.size(), 6)

        with self.assertRaises(ValidatorException):
            self.serv.createStudent(1, 2)

    def test_delete(self):
        self.serv.delStudent('1')
        self.assertEqual(self.repo.size(), 2)

        with self.assertRaises(RepositoryException):
            self.serv.delStudent(1)

        self.serv.delStudent('2')
        self.assertEqual(self.repo.size(), 1)

        with self.assertRaises(RepositoryException):
            self.serv.delStudent('ana')

        self.serv.delStudent('3')
        self.assertEqual(self.repo.size(), 0)

        with self.assertRaises(RepositoryException):
            self.serv.delStudent('234')

    def test_show(self):
        self.assertIsInstance(self.repo.get_repo()['1'], student)
        self.assertIsInstance(self.repo.get_repo()['2'], student)
        self.assertIsInstance(self.repo.get_repo()['3'], student)

    def test_modify(self):
        st1 = student('1', 'gicu')
        self.serv.modifystudent('1', st1)
        self.assertEqual(self.repo.get_repo()['1'].get_nume_student(), 'gicu')

        s1 = student('2', '3')
        with self.assertRaises(ValidatorException):
            self.serv.modifystudent('234', s1)

        st2 = student('2', 'rares')
        self.serv.modifystudent('2', st2)
        self.assertEqual(self.repo.get_repo()['2'].get_nume_student(), 'rares')

        s2 = student('ana', 'ana')
        with self.assertRaises(ValidatorException):
            self.serv.modifystudent('1', s2)

        st3 = student('3', 'marian')
        self.serv.modifystudent('3', st3)
        self.assertEqual(self.repo.get_repo()['3'].get_nume_student(), 'marian')

        st1 = student('1', 'gicu')
        with self.assertRaises(RepositoryException):
            self.serv.modifystudent('ana', st1)

        st1 = student('1', 'gicu')
        with self.assertRaises(RepositoryException):
            self.serv.modifystudent('7', st1)

    def test_find(self):

        with self.assertRaises(RepositoryException):
            self.serv.findstudent('id')

        with self.assertRaises(RepositoryException):
            self.serv.findstudent('ana')

        with self.assertRaises(RepositoryFind):
            self.serv.findstudent('7')

        with self.assertRaises(RepositoryFind):
            self.serv.findstudent('4')

    def test_generate(self):
        self.serv.generatestudents(10)
        self.assertEqual(self.repo.size(), 13)

        self.serv.generatestudents(20)
        self.assertEqual(self.repo.size(), 33)

        self.serv.generatestudents(1)
        self.assertEqual(self.repo.size(), 34)

class testStudentsRepo(unittest.TestCase):
    def setUp(self):
        self.stud1 = student('1', 'gicu')
        self.stud2 = student('2', 'florin')
        self.stud3 = student('3', 'marcel')
        self.l = StudentsRepo()
        self.l.store_student(self.stud1)
        self.l.store_student(self.stud2)
        self.l.store_student(self.stud3)

    def test_store(self):
        self.stud4 = student('4', 'nicu')
        self.l.store_student(self.stud4)
        self.assertEqual(self.l.size(), 4)

        self.stud5 = student('5', 'jean')
        self.l.store_student(self.stud5)
        self.assertEqual(self.l.size(), 5)

    def test_delete(self):
        self.l.delete_student('1')
        self.assertEqual(self.l.size(), 2)

        self.l.delete_student('2')
        self.assertEqual(self.l.size(), 1)

    def test_modify(self):
        self.new_stud1 = student('1', 'marian')
        self.l.modify_student('1', self.new_stud1)
        self.s = self.l.find_student('1')
        self.assertEqual(self.s.get_nume_student(), 'marian')
        self.assertEqual(self.s.get_id_student(), '1')

    def test_find(self):
        self.s = self.l.find_student('2')
        self.assertEqual(self.s.get_nume_student(), 'florin')
        self.assertEqual(self.s.get_id_student(), '2')

        self.s2 = self.l.find_student('3')
        self.assertEqual(self.s2.get_nume_student(), 'marcel')
        self.assertEqual(self.s2.get_id_student(), '3')

    def test_get_all(self):
        self.l2 = self.l.get_all_students()
        self.assertEqual(self.l2[0].get_id_student(), '1')
        self.assertEqual(self.l2[0].get_nume_student(), 'gicu')

        self.assertEqual(self.l2[1].get_id_student(), '2')
        self.assertEqual(self.l2[1].get_nume_student(), 'florin')

class testSubjectService(unittest.TestCase):
    def setUp(self):
        self.repo = SubjectsRepo()
        self.val = SubjectValidator()
        self.serv = SubjectService(self.repo, self.val)
        self.serv.CreateSubject('1', 'mate', 'pop')
        self.serv.CreateSubject('2', 'info', 'ion')
        self.serv.CreateSubject('3', 'fizica', 'popescu')

    def test_add(self):
        self.serv.CreateSubject('4', 'franceza', 'jean')
        self.assertEqual(self.repo.size(), 4)

        with self.assertRaises(ValidatorException):
            self.serv.CreateSubject('', 'bum', '')

        self.serv.CreateSubject('6', 'sport', 'freshman')
        self.assertEqual(self.repo.size(), 5)

        with self.assertRaises(ValidatorException):
            self.serv.CreateSubject('', '', 'ana')

        self.serv.CreateSubject('5', 'germana', 'frank')
        self.assertEqual(self.repo.size(), 6)

        with self.assertRaises(ValidatorException):
            self.serv.CreateSubject(1, 2, 3)

    def test_delete(self):
        self.serv.delSubject('1')
        self.assertEqual(self.repo.size(), 2)

        with self.assertRaises(RepositoryException):
            self.serv.delSubject(1)

        self.serv.delSubject('2')
        self.assertEqual(self.repo.size(), 1)

        with self.assertRaises(RepositoryException):
            self.serv.delSubject('ana')

        self.serv.delSubject('3')
        self.assertEqual(self.repo.size(), 0)

        with self.assertRaises(RepositoryException):
            self.serv.delSubject('234')

    def test_show(self):
        self.assertIsInstance(self.repo.get_repo()['1'], disciplina)
        self.assertIsInstance(self.repo.get_repo()['2'], disciplina)
        self.assertIsInstance(self.repo.get_repo()['3'], disciplina)

    def test_modify(self):
        sub1 = disciplina('1', 'mate', 'boss')
        self.serv.modifysubject('1', sub1)
        self.assertEqual(self.repo.get_repo()['1'].get_nume_disciplina(), 'mate')
        self.assertEqual(self.repo.get_repo()['1'].get_profesor(), 'boss')

        s1 = disciplina('2', '3', '6')
        with self.assertRaises(ValidatorException):
            self.serv.modifysubject('2', s1)

        sub2 = disciplina('2', 'sport', 'fresh')
        self.serv.modifysubject('2', sub2)
        self.assertEqual(self.repo.get_repo()['2'].get_nume_disciplina(), 'sport')
        self.assertEqual(self.repo.get_repo()['2'].get_profesor(), 'fresh')

        s2 = disciplina('ana', 'ana', 'ana')
        with self.assertRaises(ValidatorException):
            self.serv.modifysubject('1', s2)

        sub3 = disciplina('3', 'franceza', 'jean')
        self.serv.modifysubject('3', sub3)
        self.assertEqual(self.repo.get_repo()['3'].get_nume_disciplina(), 'franceza')
        self.assertEqual(self.repo.get_repo()['3'].get_profesor(), 'jean')

        s1 = disciplina('1', 'mat', 'pop')
        with self.assertRaises(RepositoryException):
            self.serv.modifysubject('ana', s1)

        s1 = disciplina('1', 'eco', 'man')
        with self.assertRaises(RepositoryException):
            self.serv.modifysubject('6', s1)

    def test_find(self):

        with self.assertRaises(RepositoryException):
            self.serv.findsubject('id')

        with self.assertRaises(RepositoryException):
            self.serv.findsubject('ana')

        with self.assertRaises(RepositoryFind):
            self.serv.findsubject('7')

        with self.assertRaises(RepositoryFind):
            self.serv.findsubject('4')

    def test_generate(self):
        self.serv.generatesubjects(10)
        self.assertEqual(self.repo.size(), 13)

        self.serv.generatesubjects(20)
        self.assertEqual(self.repo.size(), 33)

        self.serv.generatesubjects(1)
        self.assertEqual(self.repo.size(), 34)

class testSubjectRepo(unittest.TestCase):
    def setUp(self):
        self.repo = SubjectsRepo()
        self.sub1 = disciplina('1', 'mate', 'pop')
        self.sub2 = disciplina('2', 'info', 'ion')
        self.sub3 = disciplina('3', 'fizica', 'popescu')
        self.repo.store_subject(self.sub1)
        self.repo.store_subject(self.sub2)
        self.repo.store_subject(self.sub3)

    def test_store(self):
        self.assertEqual(self.repo.size(), 3)

        self.sub4 = disciplina('4', 'geo', 'gicu')
        self.repo.store_subject(self.sub4)
        self.assertEqual(self.repo.size(), 4)

        self.sub5 = disciplina('5', 'ist', 'popescu')
        self.repo.store_subject(self.sub5)
        self.assertEqual(self.repo.size(), 5)

    def test_delete(self):
        self.repo.delete_subject('1')
        self.assertEqual(self.repo.size(), 2)

        self.repo.delete_subject('2')
        self.assertEqual(self.repo.size(), 1)

        self.repo.delete_subject('3')
        self.assertEqual(self.repo.size(), 0)

    def test_modify(self):
        self.sub4 = disciplina('1', 'java', 'john')
        self.repo.modify_subject('1', self.sub4)
        self.sub = self.repo.find_subject('1')
        self.assertEqual(self.sub.get_id_disciplina(), '1')
        self.assertEqual(self.sub.get_nume_disciplina(), 'java')
        self.assertEqual(self.sub.get_profesor(), 'john')

    def test_find(self):
        self.sub = self.repo.find_subject('1')
        self.assertEqual(self.sub.get_id_disciplina(), '1')
        self.assertEqual(self.sub.get_nume_disciplina(), 'mate')
        self.assertEqual(self.sub.get_profesor(), 'pop')

    def test_size(self):
        self.assertEqual(self.repo.size(), 3)

    def test_get_all(self):
        self.l2 = self.repo.get_all_subjects()
        self.assertEqual(self.l2[0].get_id_disciplina(), '1')
        self.assertEqual(self.l2[0].get_nume_disciplina(), 'mate')
        self.assertEqual(self.l2[0].get_profesor(), 'pop')

        self.assertEqual(self.l2[1].get_id_disciplina(), '2')
        self.assertEqual(self.l2[1].get_nume_disciplina(), 'info')
        self.assertEqual(self.l2[1].get_profesor(), 'ion')

class testNoteServ(unittest.TestCase):

    def setUp(self):
        self.stud1 = student('1','matei')
        self.stud2 = student('2', 'razvan')
        self.sub1 = disciplina('1', 'mate', 'pop')
        self.sub2 = disciplina('2', 'info', 'ionescu')
        self.l_s = StudentsRepo()
        self.l_d = SubjectsRepo()
        #self.l_s_file = StudentRepositoryFile(self.l_s)
        #self.l_d_file = SubjectRepositoryFile(self.l_d)
        self.l_s.store_student(self.stud1)
        self.l_s.store_student(self.stud2)
        self.l_d.store_subject(self.sub1)
        self.l_d.store_subject(self.sub2)
        self.cat = NoteRep(self.l_s, self.l_d)
        self.cat_serv = StudentsNote(NoteRep)
        self.cat.update_note()
        self.cat.asignare_nota('1', '2', 9)
        self.cat.asignare_nota('1', '2', 8)
        self.cat.asignare_nota('2', '1', 10)
        self.cat.asignare_nota('2', '2', 4)
        self.cat.asignare_nota('2', '2', 7)

    def test_asignare(self):
        self.cat.asignare_nota('2', '2', 7)
        self.assertEqual(self.cat.get_repo(),{'1': {'1': [], '2': [9, 8]}, '2': {'1': [10], '2': [4, 7, 7]}})

        self.cat.asignare_nota('2', '1', 5)
        self.assertEqual(self.cat.get_repo(), {'1': {'1': [], '2': [9, 8]}, '2': {'1': [10, 5], '2': [4, 7, 7]}})

        self.cat.asignare_nota('1', '1', 10)
        self.assertEqual(self.cat.get_repo(), {'1': {'1': [10], '2': [9, 8]}, '2': {'1': [10, 5], '2': [4, 7, 7]}})

        self.cat.asignare_nota('1', '2', 6)
        self.assertEqual(self.cat.get_repo(), {'1': {'1': [10], '2': [9, 8, 6]}, '2': {'1': [10, 5], '2': [4, 7, 7]}})

        with self.assertRaises(RepositoryFind):
            self.cat.asignare_nota('6', '1', 10)

        with self.assertRaises(RepositoryFind):
            self.cat.asignare_nota('1', '7', 9)

        with self.assertRaises(RepositoryFind):
            self.cat.asignare_nota('10', '10', 10)

        with self.assertRaises(RepositoryException):
            self.cat.asignare_nota('m', 'm', 'm')

        with self.assertRaises(RepositoryException):
            self.cat.asignare_nota('2', 'm', 9)

        with self.assertRaises(RepositoryException):
            self.cat.asignare_nota(1, 1, 1)


    def test_afisare_note(self):
        self.assertEqual(self.cat.get_repo(), {'1': {'1': [], '2': [9, 8]}, '2': {'1': [10], '2': [4, 7]}})

        self.cat.asignare_nota('1', '1', 6)
        self.cat.asignare_nota('1', '1', 6)
        self.cat.asignare_nota('1', '1', 6)
        self.assertEqual(self.cat.get_repo(),{'1': {'1': [6, 6, 6], '2': [9, 8]}, '2': {'1': [10], '2': [4, 7]}})
        self.assertNotEqual(self.cat.get_repo(), {'1': {'1': [8, 6, 6], '2': [9, 8]}, '2': {'1': [10, 3, 2, 3], '2': [4, 7]}})


        self.cat.asignare_nota('2', '1', 3)
        self.cat.asignare_nota('2', '1', 3)
        self.cat.asignare_nota('2', '1', 3)
        self.assertEqual(self.cat.get_repo(), {'1': {'1': [6, 6, 6], '2': [9, 8]}, '2': {'1': [10, 3, 3, 3], '2': [4, 7]}})
        self.assertNotEqual(self.cat.get_repo(), {'1': {'1': [8, 6, 6], '2': [9, 8]}, '2': {'1': [10, 3, 3, 3], '2': [4, 7]}})

        self.cat.asignare_nota('1', '1', 7)
        self.cat.asignare_nota('1', '2', 7)
        self.cat.asignare_nota('1', '2', 7)
        self.assertEqual(self.cat.get_repo(), {'1': {'1': [6, 6, 6, 7], '2': [9, 8, 7, 7]}, '2': {'1': [10, 3, 3, 3], '2': [4, 7]}})

    def test_lista_dupa_nume(self):
        self.assertEqual(self.cat.lista_dupa_nume('1'), [['1', 'matei', []], ['2', 'razvan', [10]]])

        self.assertEqual(self.cat.lista_dupa_nume('2'),[['1', 'matei', [9, 8]], ['2', 'razvan', [4, 7]]])

        with self.assertRaises(RepositoryException):
            self.cat_serv.listaDupaNume('m')

        with self.assertRaises(RepositoryException):
            self.cat_serv.listaDupaNume('ana')

        with self.assertRaises(RepositoryFind):
            self.cat.lista_dupa_nume('10')

        with self.assertRaises(RepositoryFind):
            self.cat.lista_dupa_nume('4')

    def test_lista_dupa_note(self):
        self.assertEqual(self.cat.lista_dupa_nota('1'), [['2', 'razvan', [10], 10.0], ['1', 'matei', [], 0]])

        self.assertEqual(self.cat.lista_dupa_nota('2'), [['1', 'matei', [9, 8], 8.5], ['2', 'razvan', [4, 7], 5.5]])

        self.cat.asignare_nota('1', '1', 9)
        self.assertEqual(self.cat.lista_dupa_nota('1'), [['2', 'razvan', [10], 10.0], ['1', 'matei', [9], 9.0]])

        self.cat.asignare_nota('2', '2', 7)
        self.assertEqual(self.cat.lista_dupa_nota('2'), [['1', 'matei', [9, 8], 8.5], ['2', 'razvan', [4, 7, 7], 6.0]])

        with self.assertRaises(RepositoryException):
            self.cat_serv.listaDupaNote('pam')

        with self.assertRaises(RepositoryException):
            self.cat_serv.listaDupaNote('id')

        with self.assertRaises(RepositoryFind):
            self.cat.lista_dupa_nota('20')

        with self.assertRaises(RepositoryFind):
            self.cat.lista_dupa_nota('8')

    def test_statistic(self):
        pass
        #self.assertEqual(self.cat.statistici_20(), None)

class testNoteService(unittest.TestCase):
    def setUp(self):
        self.stud1 = student('1', 'matei')
        self.stud2 = student('2', 'razvan')
        self.sub1 = disciplina('1', 'mate', 'pop')
        self.sub2 = disciplina('2', 'info', 'ionescu')
        self.l_s = StudentsRepo()
        self.l_d = SubjectsRepo()
        self.val = NotaValidator()
        # self.l_s_file = StudentRepositoryFile(self.l_s)
        # self.l_d_file = SubjectRepositoryFile(self.l_d)
        self.l_s.store_student(self.stud1)
        self.l_s.store_student(self.stud2)
        self.l_d.store_subject(self.sub1)
        self.l_d.store_subject(self.sub2)
        self.cat = NoteRepo()
        self.cat_serv = ServNota(self.cat, self.val, self.l_s, self.l_d)
        self.cat_serv.asignare_nota('1', '1', 9)
        self.cat_serv.asignare_nota('1', '2', 8)
        self.cat_serv.asignare_nota('2', '1', 10)
        self.cat_serv.asignare_nota('2', '2', 4)
        self.cat_serv.asignare_nota('2', '1', 7)

    def test_asignare(self):
        with self.assertRaises(ValidatorException):
            self.cat_serv.asignare_nota('1', '2', 12)

        with self.assertRaises(ValidatorException):
            self.cat_serv.asignare_nota('1', '2', -4)

        with self.assertRaises(ValidatorException):
            self.cat_serv.asignare_nota('1', '2', 0)

        with self.assertRaises(RepositoryException):
            self.cat_serv.asignare_nota(1, '2', -4)

        with self.assertRaises(RepositoryFind):
            self.cat_serv.asignare_nota('1', '7', -4)

        with self.assertRaises(RepositoryException):
            self.cat_serv.asignare_nota('1', 2, -4)

        self.cat_serv.asignare_nota('1', '2', 10)
        self.assertEqual(self.cat.size(), 6)

        self.cat_serv.asignare_nota('2', '2', 9)
        self.assertEqual(self.cat.size(), 7)

        self.cat_serv.asignare_nota('2', '1', 4)
        self.assertEqual(self.cat.size(), 8)

        self.cat_serv.asignare_nota('1', '2', 8)
        self.assertEqual(self.cat.size(), 9)

    def test_lista_nume(self):

        self.assertEqual(self.cat_serv.lista_dupa_nume('2'),[['1', 'matei', 8.0], ['2', 'razvan', 4.0]])

        self.assertEqual(self.cat_serv.lista_dupa_nume('1'), [['1', 'matei', 9.0], ['2', 'razvan', 8.5]])

        self.cat_serv.asignare_nota('1', '2', 3)
        self.assertEqual(self.cat_serv.lista_dupa_nume('2'), [['1', 'matei', 5.5], ['2', 'razvan', 4.0]])

        self.assertEqual(self.cat_serv.lista_dupa_nume('1'), [['1', 'matei', 9.0], ['2', 'razvan', 8.5]])

        self.cat_serv.asignare_nota('2', '1', 4)
        self.assertEqual(self.cat_serv.lista_dupa_nume('1'), [['1', 'matei', 9.0], ['2', 'razvan', 7.0]])

    def test_lista_nota(self):

        self.assertEqual(self.cat_serv.lista_dupa_note('1'),[['1', 'matei', 9.0], ['2', 'razvan', 8.5]])

    def test_update(self):

        self.l_s.delete_student('1')
        self.cat_serv.update()
        self.assertEqual(self.cat_serv.afisare_note(),[['razvan', 'mate', 10], ['razvan', 'info', 4], ['razvan', 'mate', 7]])

class testConsole(unittest.TestCase):
    def setUp(self):
        self.stud_repo = StudentsRepo()
        self.sub_repo = SubjectsRepo()
        self.val_stud = StudentValidator()
        self.val_sub = SubjectValidator()
        self.stud_serv = StudentService(self.stud_repo, self.val_stud)
        self.sub_serv = SubjectService(self.sub_repo, self.val_sub)
        self.note_repo = NoteRepo()
        self.val_nota = NotaValidator()
        self.note_serv = ServNota(self.note_repo, self.val_nota, self.stud_repo, self.sub_repo)
        #self.ui = Console(self.stud_serv, self.sub_serv, self.note_serv)

    def test_asignare(self):
        pass

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

class testFileStudentRepo(unittest.TestCase):
    def setUp(self):
        #self.stud_repo = StudentsRepo()
        self.file = ('test_students_file')
        self.stud_repo_file = StudentRepositoryFile(self.file)
        self.stud_repo = StudentsRepo()
        t.clearFile(self.file)

    def test_store(self):
        self.stud = student('11', 'gicu')
        self.stud_repo_file.store_student(self.stud)
        self.assertEqual(self.stud_repo_file.size(), 1)

    def test_create(self):
        self.line = '1 marinel\n'
        self.st = self.stud_repo_file.createStudentFromLine(self.line)
        self.assertEqual(self.st.get_id_student(), '1')
        self.assertEqual(self.st.get_nume_student(), 'marinel')

    def test_load(self):
        self.stud_repo_file.loadFromFile()
        self.assertEqual(self.stud_repo.size(), 0)


class testFileSubjectRepo(unittest.TestCase):
    def setUp(self):
        #self.stud_repo = StudentsRepo()
        self.file = ('test_subjects_file')
        t.clearFile(self.file)
        self.sub_repo_file = SubjectRepositoryFile(self.file)
        self.sub_repo = SubjectsRepo()

    def test_store(self):
        self.sub = disciplina('1', 'mate', 'pop')
        self.sub_repo_file.store_subject(self.sub)
        self.assertEqual(self.sub_repo_file.size(), 1)

    def test_create(self):
        self.line = '1 marinel pop\n'
        self.st = self.sub_repo_file.createSubjectFromLine(self.line)
        self.assertEqual(self.st.get_id_disciplina(), '1')
        self.assertEqual(self.st.get_nume_disciplina(), 'marinel')
        self.assertEqual(self.st.get_profesor(), 'pop')

    def test_load(self):
        self.sub_repo_file.loadFromFile()
        self.assertEqual(self.sub_repo.size(), 0)


class testFileNoteRepo(unittest.TestCase):
    def setUp(self):
        self.file = ('test_note_file')
        self.note_repo_file = NoteRepoFile(self.file)
        t.clearFile(self.file)

    def test_store(self):
        self.nota = Nota('1', '1', '10')
        self.note_repo_file.asignareNota(self.nota)
        self.assertEqual(self.note_repo_file.size(), 1)

    def test_create(self):
        self.line = '1 1 10\n'
        self.n = self.note_repo_file.createNotaFromLine(self.line)
        self.assertEqual(self.n[0].get_id_student(), '1')
        self.assertEqual(self.n[0].get_id_disciplina(), '1')
        self.assertEqual(self.n[0].get_n(), '10')

class testTools(unittest.TestCase):
    """
    teste blackbox
    se iau datele de intrare si se verifica daca functia returneaza true sau false
    """
    def test_verify_nume(self):
        self.assertEqual(t.verify_nume('ana'), 1)
        self.assertEqual(t.verify_nume('bogdan'), 1)
        self.assertEqual(t.verify_nume('matei'), 1)
        self.assertEqual(t.verify_nume('r322'), 0)
        self.assertEqual(t.verify_nume('908'), 0)

    def tesy_verify_int(self):
        self.assertEqual(t.verify_int('ana'), 0)
        self.assertEqual(t.verify_int('bogdan'), 0)
        self.assertEqual(t.verify_int('matei'), 0)
        self.assertEqual(t.verify_int('322'), 1)
        self.assertEqual(t.verify_int('10'), 1)

class testValidators(unittest.TestCase):
    def setUp(self):
        self.val_stud = StudentValidator()
        self.val_sub = SubjectValidator()
        self.stud1 = student('1', '')
        self.stud2 = student('', 'gicu')
        self.stud3 = student('3', '3')
        self.sub1 = disciplina('1', '', 'pop')
        self.sub2 = disciplina('', 'info', '')
        self.sub3 = disciplina('3', '3', 'popescu')

    def test_student(self):
        with self.assertRaises(ValidatorException):
            self.val_stud.validate(self.stud1)

        with self.assertRaises(ValidatorException):
            self.val_stud.validate(self.stud2)

        with self.assertRaises(ValidatorException):
            self.val_stud.validate(self.stud3)

    def test_subject(self):
        with self.assertRaises(ValidatorException):
            self.val_sub.validate(self.sub1)

        with self.assertRaises(ValidatorException):
            self.val_sub.validate(self.sub2)

        with self.assertRaises(ValidatorException):
            self.val_sub.validate(self.sub3)


if __name__ == '__main__':
    unittest.main()
