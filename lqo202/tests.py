"""
This was an attempt of writing a test.
The idea was to verify that the code assignemnt8 just runs with 1,2,q values otherwise enters the loop
"""

import unittest
import assignment8 as as8


__author__ = 'luisa:lqo202'



class TestInvestment(unittest.TestCase):
    def testloop_possibleanswers(self):
        #Listing for test
        listyesanswer = [1, 2, 'q']
        listnoanswer = ['b','a']

        #Testing the lists
        for answer in listyesanswer:
            #as8.callback=self.assertIn(answer,listyesanswer)
            self.failIf(as8.captureanswernotq([answer]))

        for answer in listnoanswer:
            #self.assertIn(answer,listyesanswer)
            self.failIf(as8.captureanswernotq([answer]))

if __name__ == '__main__':
    unittest.main()
