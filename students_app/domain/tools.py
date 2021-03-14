
def verify_nume(nume):
    return nume.isalpha()

def verify_int(n):
    return n.isnumeric()

def is_nume(n):
        try:
            assert verify_nume(n) == True
        except (AssertionError, AttributeError, ValueError):
            return 0

def is_int(n):
        try:
            assert verify_int(n) == True
        except (ValueError, AssertionError, AttributeError):
            return 0

def read_command(t):
    while True:
        try:
            c = input(t)
            assert verify_int(c) == True
            return c
        except (ValueError, AssertionError, AttributeError):
            print("Ati introdus gresit! ")

def clearFile(fileName):
    """
    function that clears a filee
    :param fileName: numele fisierului
    """
    f = open(fileName, "w")
    f.close()
