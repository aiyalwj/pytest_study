# fighting AX
# 2025/5/6 13:36

import unittest

from unittest_study.hm_05_demo1 import TestAdd

suit = unittest.TestSuite()

suit.addTest(unittest.makeSuite(TestAdd))

runner = unittest.TextTestRunner()

runner.run(suit)