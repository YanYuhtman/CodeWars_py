import unittest
import itertools as I
import functools as F
import numpy as N
import operator as O


# is_check = lambda board: True
def is_check(board):
    # tmp = None
    # mL = list()
    # for y,s in enumerate(board):
    #    for x,s in enumerate(s):
    #         mL += [[y,x,s]]
    #
    # tmp = (list(map(lambda y : list(map(lambda x: [y[0],x[0],x[1]],enumerate(y[1]))), enumerate(board))))
    # tmp = list(map(lambda y: list(map(lambda x: [y[0],x[0],x[1]],enumerate(y[1]))), enumerate(board)))

    tmp = (filter(lambda v:v[2]!=' ',F.reduce(lambda a,b:a+b,[(list(map(lambda X:(Y[0],X[0],X[1]),enumerate(Y[1])))) for Y in enumerate(board)])))
    tmp = sorted(tmp,key=lambda x:x[2])
    tmp = list(map(lambda t:(t[0]-tmp[0][0],t[1]-tmp[0][1],t[2]),tmp))
    tmp = list(map(lambda t:(abs(int(t[0]/t[1]) if t[1] else 0),t[0]**2+t[1]**2,t[2]),tmp))
    # tmp = F.reduce(lambda a,b: l + b,tmp)
    tmp = N.unique(sorted(tmp,key=lambda x:x[1]),axis=1)
    tmp = list(map(lambda t:(
         {'♞':t[1]=='5',
         '♝':t[0]=='1',
         '♟':t[1]=='2',
         '♜':t[0]=='0',
         '♛':(t[1]=='1' or t[0]=='0')
         }
        .get(t[2])),tmp))
    return any(tmp)
    # tmp = [((list(Y[1])) for X in enumerate(Y[1])) for Y in enumerate(board)]


    tmp = list(map(lambda by:
               list(map(lambda bx:(bx[1],by[0],bx[0]),enumerate(by[1]))),enumerate(board)))
    True
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
