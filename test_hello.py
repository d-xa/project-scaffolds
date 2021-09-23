#!/usr/bin/env python

import unittest
from hello import hello


class Testing(unittest.TestCase):
    def test_string(self):
        a = hello()
        b = 'Hello Python'
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
