import unittest

from src.python_package_sample import sample_function


class TestSampleModules(unittest.TestCase):
    def test_sample_function(self):
        """python_package_sample/sample_modules/sample_function()のテスト

        """
        print('run a test of sample_function')
        self.assertEqual("Hello sample function!!!", sample_function())


if __name__ == '__main__':
    unittest.main()
