import unittest
from itertools import *
from functools import *
import numpy as N
import operator as O


# is_check=lambda b:any(map(lambda t:({'♞':t[1]==5,'♝':t[0]==1,'♟':t[1]==2,'♜':t[0]==0,'♛':(t[1]==1 or t[0]==0)}[t[2]]),dict(map(lambda t:(t[0],t),sorted(dropwhile(lambda t:t[2]=='♔',map(lambda t:(abs(t[0]/t[1] if t[1] else 0),t[0]**2+t[1]**2,t[2]),(lambda b:map(lambda t:(t[0]-b[0][0],t[1]-b[0][1],t[2]),b))(sorted([[x,y,b[x][y]]for x in range(0,8)for y in range(0,8)if b[x][y]!=' '],key=lambda x:x[2])))),key=lambda t:t[1],reverse=True))).values()))

def is_check(b):

    # tmp = (filter(lambda v:v[2]!=' ',reduce(lambda a,b:a+b,[(list(map(lambda X:(Y[0],X[0],X[1]),enumerate(Y[1])))) for Y in enumerate(b)])))
    tmp = [[b[x][y],x,y]for x in range(0,8)for y in range(0,8)if b[x][y]!=' ']
    tmp = sorted(tmp)
    tmp = (lambda b:map(lambda t:(t[0],t[1]-b[0][1],t[2]-b[0][2]),b))(tmp)
    tmp = map(lambda t:(t[0],abs(not t[2]or t[1]/t[2]),t[1]**2+t[2]**2),tmp)
    # tmp = list(tmp).pop()
    tmp = dropwhile(lambda t:t[0]=='♔',tmp)
    tmp = dict(map(lambda t:(t[1],t),sorted(tmp)))
    tmp = map(lambda t:(
         {'♞':t[2]==5,
         '♝':t[1]==1,
         '♟':t[2]==2,
         '♜':t[1]==0,
         '♛':(t[2]==1or t[1]==0)
         }[t[0]]),tmp.values())
    return any(tmp)
class MyTestCase(unittest.TestCase):
    is_check = lambda board: False

    def test_noTest(self):
        is_check([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', '♟', ' ', ' ', ' ', ' '],
                  [' ', ' ', '♔', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        self.assertEqual(True,True)

    def test_PawnCheck(self):
        self.assertEqual(is_check([[' ',' ',' ',' ',' ',' ',' ',' '],
                                   [' ',' ',' ',' ',' ',' ',' ',' '],
                                   [' ',' ',' ',' ',' ',' ',' ',' '],
                                   [' ',' ',' ',' ',' ',' ',' ',' '],
                                   [' ',' ',' ','♟',' ',' ',' ',' '],
                                   [' ',' ','♔',' ',' ',' ',' ',' '],
                                   [' ',' ',' ',' ',' ',' ',' ',' '],
                                   [' ',' ',' ',' ',' ',' ',' ',' ']]),
                         True,"Pawn check")

    def test_Pawn_no_check(self):
        self.assertEqual(is_check([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', '♟', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', '♔', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]),
                         False,"Pawn no check")

    def test_Bishop_check(self):
        self.assertEqual(is_check([[' ', ' ', ' ', ' ', ' ', ' ', ' ', '♝'],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    ['♔', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]),
                          True,"Bishop check")

    def test_Rook_check(self):
        self.assertEqual(is_check([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', '♔', ' ', ' ', '♜', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]),
                         True,"Rook check")

    def test_Knight_check(self):
       self.assertEqual(is_check([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', '♔', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  ['♞', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]),
                        True,"Knight check")

    def test_Queen_check(self):
       self.assertEqual(is_check([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  ['♛', ' ', '♔', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]),
                        True,"Queen check")

    def test_None(self):
       self.assertEqual(is_check([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', '♔', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]),
                        False, "No check")

    def test_Multiple_no_check(self):
       self.assertEqual(is_check([['♛', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', '♞'],
                                  [' ', ' ', '♔', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', '♛', ' ', ' ', ' ', '♞']]),
                        False,"Multiple no check")

    def test_Multiple_no_check2(self):
        self.assertEqual(is_check([['♛', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', '♞'],
                                   [' ', ' ', '♔', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', '♛', ' ', ' ', ' ', '♞']]),
                         False,"Multiple no check 2")

    def test_Multiple_no_check3(self):
        self.assertEqual(is_check([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   ['♔', ' ', ' ', ' ', ' ', ' ', ' ', '♞'],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]),
                         False,"Multiple no check 3")


if __name__ == '__main__':
    unittest.main()
