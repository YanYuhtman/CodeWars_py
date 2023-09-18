import unittest
import numpy as np
#https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python


def spiralize0(size) -> np.array:
    board = np.array([[1 for _ in range(0,size)] for _ in range(0, size)])

    x, y = (0, 1)
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    l = len(board) - 2

    while l >= 1:
        for s in steps:
            m = steps.index(s) % 4
            if m == 1 or m == 3:
                l -= 1 if (l == len(board) - 2) == 1 else 2
            for i in range(0, l):
                board[y][x] = 0
                y += s[1]
                x += s[0]
    board[y][x] = 0
    return board


#NOT MINE - COOL :D
def spiralize(size):
    # Make a snake
    spiral = np.array([[1 - min(i,j,size-max(i,j)-1)%2 for j in range(size)] for i in range(size)])
    for i in range(size//2-(size%4==0)):
      spiral[i+1][i] = 1 - spiral[i+1][i]
    return spiral
class MyTestCase(unittest.TestCase):
    def test1(self):
        arr = np.array([[1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 1],
                  [1, 1, 1, 0, 1],
                  [1, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1]], dtype=np.int32)
        self.assertTrue(np.array_equal(spiralize(5),arr))

    def test2(self):
        arr = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
                                          [0, 0, 0, 0, 0, 0, 0, 1],
                                          [1, 1, 1, 1, 1, 1, 0, 1],
                                          [1, 0, 0, 0, 0, 1, 0, 1],
                                          [1, 0, 1, 0, 0, 1, 0, 1],
                                          [1, 0, 1, 1, 1, 1, 0, 1],
                                          [1, 0, 0, 0, 0, 0, 0, 1],
                                          [1, 1, 1, 1, 1, 1, 1, 1]])
        self.assertTrue(np.array_equal(spiralize(8), arr))

    def test3(self):
        arr = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 1],
                                 [1, 1, 1, 1, 1, 1, 1, 0, 1],
                                 [1, 0, 0, 0, 0, 0, 1, 0, 1],
                                 [1, 0, 1, 1, 1, 0, 1, 0, 1],
                                 [1, 0, 1, 0, 0, 0, 1, 0, 1],
                                 [1, 0, 1, 1, 1, 1, 1, 0, 1],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 1],
                                 [1, 1, 1, 1, 1, 1, 1, 1, 1]])
        self.assertTrue(np.array_equal(spiralize(9),
                         arr))


if __name__ == '__main__':
    unittest.main()
