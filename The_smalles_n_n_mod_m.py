import time
import unittest
from math import sqrt
from math import log
from math import ceil


#https://www.codewars.com/kata/638b4205f418c4ab857f2692



def gcd(n:int, m:int) -> int:
    while m != 0:
        n,m = m, n% m
    return n

    # tmp_n = n
    # reminder = n % m
    # while reminder != 0:
    #     tmp_n = (tmp_n - reminder)//(tmp_n//m)
    #     m = reminder
    #     reminder = tmp_n % m
    # return m if m != 1 else n

def f1(m:int) -> int:
    divSet = list()
    i = 1
    while i < m:
        i += 1
        if i < ceil(log(m,i)):
            continue
        g = gcd(m, i)
        if g != m and g > i:
            i = g
        divSet.append((m,i,g))


    return False


# def divs0(m:int) -> set:
#     a = set()
#     c = 2
#     sr = sqrt(m)
#     while m > 1:
#         while m % c == 0:
#             m = m // c
#             a.add(c)
#         c += 1
#         if len(a) == 0 and c > sr:
#             print("The number %d is prime:" % m)
#             a.add(int(m))
#             return a
#     return a


def primalityTest(n:int)->bool:
    return n == 2 or (n % 2 != 0 and pow(2,(n-1),n)==1)


def divs(m:int) -> set:
    a = set()
    c = 2
    sr = sqrt(m)
    while m > 1:
        while m % c == 0:
            m = m // c
            sr = sqrt(m)
            a.add(c)
        c += m % c
        if m > 1 and (primalityTest(m) or c > sr):
            print("The number %d is prime:" % m)
            a.add(m)
            return a
    return a


class Timer:
    start:float
    label:str
    def __init__(self,start:int=0,label = ""):
        self.start = time.time()*1000
        self.label = label
        # print("Start time: %s %d" % (self.label, self.start))

    def __str__(self) -> str:
        return ("Timer: " + self.label + " elapsed " + str((time.time()*1000) - self.start)
                + " msec")



def f(m:int) -> int:
    if m == 1:
        return 1
    if primalityTest(m):
        return m

    divsTimer = Timer(label="Primes timer for m=" + str(m))
    s = sorted(list(divs(m)))

    print("Primes: [" + ", ".join(map(str,s)) + "]")

    print(divsTimer)

    powerTimer = Timer(label="Power timer for m=" + str(m))
    insertions = 0
    while insertions < 2:
        n = 1
        for x in s:
            n = n * x
            # a little to save but a lot to calculate
            # if n < log(m,n):
            #     continue
            if pow(n,n,m) == 0:
                print(powerTimer)
                print("Found n: %d ^2=%d mod(%d), ^3=%d mod(%d)" % (n,n**2%m,m,n**3%m,m))
                return n
        s.insert(0,2)
        insertions +=1




class MyTestCase(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd(945,399), 21)
        self.assertEqual(gcd(18, 6), 6)
        self.assertEqual(gcd(1444764, 8766), 6)
        self.assertEqual(gcd(13, 5), 1)


    def test_primality(self):
        self.assertEqual(primalityTest(2), True)
        self.assertEqual(primalityTest(3), True)
        self.assertEqual(primalityTest(5), True)
        self.assertEqual(primalityTest(13), True)
        self.assertEqual(primalityTest(17377), True)
        self.assertEqual(primalityTest(17378), False)
        self.assertEqual(primalityTest(81), False)
        self.assertEqual(primalityTest(9737333), True)
        self.assertEqual(primalityTest(174440041), True)
        self.assertEqual(primalityTest(222334565193649), True)


    def test_s(self):
        self.assertEqual(f(666), 222)
        self.assertEqual(f(1), 1)
        self.assertEqual(f(2), 2)
        self.assertEqual(f(8), 4)
        self.assertEqual(f(81), 6)
        self.assertEqual(f(384), 12)
        self.assertEqual(f(13), 13)
        self.assertEqual(f(420), 210)
        self.assertEqual(f(1234567890), 411522630)

    def test_hard(self):
        # self.assertEqual(f(811), 811)
        self.assertEqual(f(657721), 811)
        # self.assertEqual(f(533411731), 811)
        # self.assertEqual(f(432596913841), 811)
        # self.assertEqual(f(350836097125051), 811)
        # self.assertEqual(f(284528074768416361), 811)
        # self.assertEqual(f(230752268637185668771), 811)

    def test_10_9(self):
        self.assertEqual(f(153177707), 153177707)
        self.assertEqual(f(662558756), 331279378)
        self.assertEqual(f(492185007), 164061669)
        self.assertEqual(f(804525804), 44695878)
    def test_10_18(self):
        self.assertEqual(f(151139185544638995), 151139185544638995)
        self.assertEqual(f(229340832900061929), 229340832900061929)
        self.assertEqual(f(771664430788135076), 385832215394067538)
        self.assertEqual(f(183505472281088053), 183505472281088053)
        self.assertEqual(f(683316963595419586), 683316963595419586)
        self.assertEqual(f(881579821966452820), 440789910983226410)

        self.assertEqual(f(723933524240285107), 723933524240285107)
        self.assertEqual(f(351826822115882012), 175913411057941006)
        self.assertEqual(f(723933524240285107), 723933524240285107)

        self.assertEqual(f(304951420396289928), 76237855099072482)

        # self.assertEqual(f(860991034399103123), 860991034399103123)


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
