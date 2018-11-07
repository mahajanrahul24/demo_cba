# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:06:05 2018

@author: rahulm99
"""

import unittest 
#from inc_demo import inc
import inc

class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(inc.inc(0), 1)
        self.assertEqual(inc.inc(100), 101)
        self.assertEqual(inc.inc(1), 2)
        self.assertEqual(inc.inc(-1), 0)
        self.assertEqual(inc.inc(4), 5)
        
        
if __name__ == '__main__':
    unittest.main()   