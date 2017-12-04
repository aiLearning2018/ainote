import unittest

import count_words as cw

class TestCountWord(unittest.TestCase):
    @staticmethod
    def invoke_result(num):
        return cw.count_words("betty bought a bit of butter but the butter was bitter", num)

    def test_count_number(self):
        result = TestCountWord.invoke_result(3)
        self.assertEquals(3, len(result))

    def test_result(self):
        result = TestCountWord.invoke_result(3)
        self.assertEquals([('butter', 2), ('a', 1), ('betty', 1)], result)


if __name__ == '__main__':
    unittest.main()