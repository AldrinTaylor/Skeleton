import unittest;

from skeleton import main;

class TestCase(unittest.TestCase):

    def test_func(self):
        self.assertEqual(main.func(),'Hello World!');


if __name__ == '__main__':
    unittest.main();
