from repository.note_repository import NoteRepo
from domain.entities import Nota
import fileinput


class NoteRepoFile(NoteRepo):
    def __init__(self, fileName):
        NoteRepo.__init__(self)
        self.__fileName = fileName
        self.__loadFromFile()

    def createNotaFromLine(self, line):
        """
        Process the a line from the file and create a student
        return student
        """
        fields = line.split()
        l_note = []
        for i in range(2, len(fields)):
            nota = Nota(fields[0], fields[1], fields[i])
            l_note.append(nota)
        return l_note

    def __loadFromFile(self):
        fh = open(self.__fileName)
        for line in fh:
            if line.strip() == " ":
                continue  # we have an empty line, just skip
            l = self.createNotaFromLine(line)
            # invoke the store method from the base class
            for item in l:
                NoteRepo.asignareNota(self, item)

        fh.close()

    def asignareNota(self, n):
        # invoke store method from the base class
        NoteRepo.asignareNota(self, n)
        self.__appendToFile(n)

    def __appendToFile(self, n):
        """
          Append a new line in the file representing the student st
        """
        fh = open(self.__fileName, "a")
        line = n.get_id_student() + " " + n.get_id_disciplina() + " " + n.get_n()
        #fh.write("\n")
        fh.write('%s\n' %line)
        fh.close()
"""
    def find(self, id_stud, id_sub):
        fh = open(self.__fileName)
        for i, line in enumerate(fh):
            if line.strip() == " ":
                continue  # we have an empty line, just skip
            l = self.__createNotaFromLine(line)
            # invoke the store method from the base class
            for item in l:
                if item.get_id_student() == id_stud and item.get_id_disciplina() == id_sub:
                    return item
        fh.close()

    def del_nota(self, id_stud, id_sub):
        with fileinput.FileInput(self.__fileName, inplace=True) as f:
            for line in f:
                l = self.__createNotaFromLine(line)
                for item in l:
                    if item.get_id_student() == id_stud and item.get_id_disciplina() == id_sub:
                        continue
                    else:
                        print(line, end='')
"""