import unittest


# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail_rec(map: [[]], res: []) -> []:
    n = len(map)
    if n <= 1:
        if n == 1 and len(map[0]) == 1:
            res.append(map[0][0])
        return res

    p = (0, 0)
    side = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for s in side:
        step = 1
        while True:
            res.append(map[p[1]][p[0]])
            p = (p[0] + s[0], p[1] + s[1])
            step += 1
            if step >= n:
                break

    next_map:list = []
    for r in map[1:n-1]:
        tmp_row = []
        for c in r[1:n-1]:
            tmp_row.append(c)
        next_map.append(tmp_row)
    return snail_rec(next_map, res)


def snail(snail_map):
    return snail_rec(snail_map, [])

class MyTestCase(unittest.TestCase):
    def test_empty(self):
        array = [[]]
        expected = []
        self.assertEqual(expected, snail(array))  # add assertion here
    def test_1(self):
        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(expected, snail(array))  # add assertion here

    def test_2(self):
        array = [[1, 2, 3],
                 [8, 9, 4],
                 [7, 6, 5]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(expected, snail(array))  # add assertion here

    def test_3(self):
        array = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]]
        expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.assertEqual(expected, snail(array))  # add assertion here


if __name__ == '__main__':
    unittest.main()
