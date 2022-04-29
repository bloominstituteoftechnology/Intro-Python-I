import unittest
import os
import sys
import inspect


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


import hello
import bignum
import datatypes
import modules
import printing
import lists
import tuples
import slices
import comprehensions as comp
import dictionaries as dicts
import functions
import args
import scopes
import file_io
import cal
import classes
import stretch


class ModuleTest(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello.HELLO, 'Hello, world!')

    def test_bignum(self):
        self.assertEqual(bignum.BIGNUM, 2**65536)

    def test_datatypes(self):
        self.assertIsInstance(datatypes.xy_int, int)
        self.assertNotIsInstance(datatypes.xy_str, int)

    def test_modules(self):
        self.assertEqual(modules.platform, sys.platform)
        self.assertEqual(modules.python_version, sys.version)
        self.assertEqual(modules.proc_id, os.getpid())
        self.assertEqual(modules.cwd, os.getcwd())
        self.assertEqual(modules.login_name, os.getlogin())

    def test_printing(self):
        x = printing.x
        y = printing.y
        z = printing.z
        case = 'x is 10, y is 2.25, z is "I like turtles!"'
        self.assertEqual(printing.format_1, case)
        self.assertEqual(printing.format_2, case)
        self.assertEqual(printing.format_3, case)

    def test_lists(self):
        self.assertEqual(lists.length, 7)
        self.assertListEqual(lists.x, [1, 2, 3, 4, 9, 99, 10])
        self.assertListEqual(lists.list_comp, [n * 1000 for n in lists.x])

    def test_tuples(self):
        self.assertIsInstance(tuples.u, tuple)

    def test_slices(self):
        self.assertEqual(slices.a[1], 4)
        self.assertEqual(slices.a[-2], 9)
        self.assertListEqual(slices.a[3:], [7, 9, 6])
        self.assertListEqual(slices.a[2:-2], [1, 7])
        self.assertListEqual(slices.a[1:], [4, 1, 7, 9, 6])
        self.assertListEqual(slices.a[:-1], [2, 4, 1, 7, 9])
        self.assertEqual(slices.s[7:12], 'world')

    def test_comprehension(self):
        local = [1, 2, 3, 4, 5]
        y4 = [int(n) for n in local if int(n) % 2 == 0]
        self.assertListEqual(comp.y, [1, 2, 3, 4, 5])
        self.assertListEqual(comp.y2,
                             [0, 1, 8, 27, 64, 125, 216, 343, 512, 729])
        self.assertListEqual(comp.y3, ['FOO', 'BAR', 'BAZ'])
        self.assertEqual(len(y4), 2)

    def test_dictionaries(self):
        self.assertEqual(len(dicts.waypoints), 4)
        self.assertTrue(dicts.waypoints[0]['lon'], -130)
        self.assertTrue(dicts.waypoints[0]['name'], "not a real place")

    def test_functions(self):
        even = 4
        odd = 1
        self.assertEqual(functions.is_even(even), True)
        self.assertFalse(functions.is_even(odd), True)

    def test_args(self):
        self.assertEqual(args.f1(1, 2), 3)
        self.assertEqual(args.f2(1, 2, 3), 6)
        self.assertEqual(args.f3(8), 9)

    def test_scopes(self):
        self.assertTrue(scopes.x, 99)
        self.assertTrue(scopes.outer, 999)

    def test_file_io(self):
        self.assertIsInstance(file_io.foo, str)
        self.assertIsInstance(file_io.bar, str)

    def test_cal(self):
        self.assertIsInstance(cal.today.year, int)
        self.assertIsInstance(cal.today.month, int)

    def test_classes(self):
        self.assertTrue(classes.waypoint.name, "Catacombs")
        self.assertTrue(classes.geocache.size, 2)


if __name__ == "__main__":
    unittest.main()
