
from nnf import Var

def theory():
    # Define Variables
    A, B, C = map(Var, 'abc')

    # TODO: Create and return a theory that matches (A or B) and ((not A) or C)
    return A & B & C # This is the wrong answer!!

if __name__ == "__main__":
    print("Theory: %s" % str(theory()))
