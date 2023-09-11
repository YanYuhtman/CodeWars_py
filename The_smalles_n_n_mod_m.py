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

_primesSet = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 341, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 561, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 645, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1105, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1387, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1729, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1905, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2047, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2465, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2701, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2821, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3277, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491}

def primalityTest(n:int)->bool:
    return n == 2 or (n % 2 != 0 and pow(2,(n-1),n)==1)

class PrimeDict(dict):
    def add_update(self, p: int):
        self[p] = 1 if p not in self.keys() else self[p] + 1

    def toMultList(self):
        s = set()



def divs(m:int) -> set:
    a = set()
    c = 2
    sr = sqrt(m)
    primesList = sorted(list(_primesSet))
    lastPrimeIndex = 0
    while m > 1:
        while m % c == 0:
            m = m // c
            sr = sqrt(m)
            a.add(c)
            _primesSet.add(c)
        c = primesList[lastPrimeIndex] if lastPrimeIndex < len(primesList) else c + m % c
        lastPrimeIndex+=1
        if m > 1 and (primalityTest(m) or c > sr):
            print("The number %d is prime:" % m)
            a.add(m)
            _primesSet.add(m)
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
            if pow(n,n,m) == 0:
                print(powerTimer)
                print("Found n: %d ^2=%d mod(%d), ^3=%d mod(%d)" % (n,n**2%m,m,n**3%m,m))
                return n
        s.insert(0,2)
        insertions +=1




class MyTestCase(unittest.TestCase):

    # def test_generate_primes(self):
    #     primes = [2,3,5,7,11]
    #
    #     while len(primes) < 500:
    #         lastPrime = primes[len(primes)-1]
    #         while True:
    #             lastPrime += 1
    #             if primalityTest(lastPrime):
    #                 primes.append(lastPrime)
    #                 break
    #     end = True


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
        # self.assertEqual(f(169), 13)
        self.assertEqual(f(666), 222)
        # self.assertEqual(f(1), 1)
        # self.assertEqual(f(2), 2)
        # self.assertEqual(f(8), 4)
        # self.assertEqual(f(81), 6)
        # self.assertEqual(f(384), 12)
        # self.assertEqual(f(13), 13)
        # self.assertEqual(f(420), 210)
        # self.assertEqual(f(1234567890), 411522630)

    def test_hard(self):
        self.assertEqual(f(811), 811)
        self.assertEqual(f(657721), 811)
        self.assertEqual(f(533411731), 811)


        self.assertEqual(f(432596913841), 811)
        self.assertEqual(f(350836097125051), 811)
        self.assertEqual(f(284528074768416361), 811)
        self.assertEqual(f(230752268637185668771), 811)

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

        self.assertEqual(f(860991034399103123), 860991034399103123)

    def test_more_hard_tests(self):
        self.assertEqual(f(512),8)
        self.assertEqual(f(1024), 8)
        self.assertEqual(f(2048), 8)
        self.assertEqual(f(4096), 8)
        self.assertEqual(f(268435456), 16)

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
