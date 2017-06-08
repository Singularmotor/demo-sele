#coding=utf-8
import unittest

class test(unittest.TestCase):
    def testminus(self):
        result=10/2
        hope=6
        self.assertEqual(result,hope)

if __name__=="__main__":
    unittest.main()