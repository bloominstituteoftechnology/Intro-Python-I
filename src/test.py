import random
import sympy
import unittest

import sieve

class TestSieve(unittest.TestCase):
    def test_first_1000(self):
        for i in range(1001):
            self.assertEqual(sieve.is_prime(i), sympy.isprime(i))
            
    def test_10_random(self):
        for i in range(10):
            n = random.randint(2, 10000)
            self.assertEqual(sieve.is_prime(n), sympy.isprime(n))
            
if __name__ == '__main__':
    unittest.main()
