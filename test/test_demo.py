import unittest

class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def test_case01(self):
        print("test_case01")
        self.assertEqual(1,1)
        self.assertIn('h',"this")

    def test_case02(self):
        print("test_case02")
        self.assertEqual(2,2)

    @unittest.skipIf(1+1==2,"跳过")
    def test_case03(self):
        print("test_case03")
        self.assertEqual(3,3)

class demo1(unittest.TestCase):
    def test_case04(self):
        print("test_case04")
        self.assertEqual(4,4)

    def test_case05(self):
        print("test_case05")
        self.assertEqual(5,5)

class demo2(unittest.TestCase):
    def test_case06(self):
        print("test_case06")
        self.assertEqual(6,6)


if __name__ == '__main__':
    unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(demo("test_case01"))
    # suite.addTest(demo1("test_case04"))
    # unittest.TextTestRunner().run(suite)

    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(demo2)
    # suite = unittest.TestSuite([suite1,suite2])
    # unittest.TextTestRunner().run(suite)

    # discover = unittest.defaultTestLoader.discover("./","test*.py")
    # unittest.TextTestRunner().run(discover)