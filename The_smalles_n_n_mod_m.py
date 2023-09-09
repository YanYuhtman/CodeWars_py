import unittest
from math import sqrt


#https://www.codewars.com/kata/638b4205f418c4ab857f2692


def divs(m:int) -> set:
    a = set()
    c = 2
    sr = sqrt(m)
    while m > 1:
        while m % c == 0:
            m = m / c
            a.add(c)
        c += 1
        if len(a) == 0 and c > sr:
            print("The number %d is prime:" % m)
            a.add(m)
            return a
    return a

def f(m:int) -> int:
    if m == 1:
        return 1
    s = list(divs(m))
    while True:
        n = 1
        for x in s:
            n = n * x
            if pow(n,n,m) == 0:
                return n
        s.append(2)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


    def test_s(self):
        self.assertEqual(f(1), 1)
        self.assertEqual(f(2), 2)
        self.assertEqual(f(8), 4)
        self.assertEqual(f(81), 6)
        self.assertEqual(f(384), 12)
        self.assertEqual(f(13), 13)
        self.assertEqual(f(420), 210)
        self.assertEqual(f(1234567890), 411522630)


    def test_pretest(self):
        m = 222334565193649
        # m = 420
        print("mults: " + "".join(map(str, [[x] for x in divs(m)])))

        m = 419
        while m < 420:
            m+=1
            while True:
                n = 2
                while pow(n,n,m) != 0:
                    n+=1
                if n != m:
                    break
                m += 1

            print("n^n=%d n=%d m=%d" % (n**n,n,m))
            print("mults: "+ "".join(map(str, [[x] for x in range(2,m) if m % x == 0])))

if __name__ == '__main__':
    unittest.main()
