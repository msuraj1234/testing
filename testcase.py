import unittest
import stringop

class test_stringOp(unittest.TestCase):



    def setUp(self):
        print('----------------SETUP------------')

    def tearDown(self):
        print('----------------TEARDOWN------------')

    def test_concat(self):
        a = stringop.stgconcat('suraj','mazumdar')
        self.assertEqual(a,'surajmazumdar')
        print('----First')

    def test_upper(self):
        a = stringop.uppercase('suraj')
        self.assertEqual(a,'SURAJ')
        print('----Second')

    @classmethod
    def tearDownClass(cls):
        print('----------teardownClass----')

if __name__ == '__main__':
    unittest.main()