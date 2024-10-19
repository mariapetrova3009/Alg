import unittest
from time import perf_counter
from lab2.task9.src.task9 import strassen
class TestStrassen(unittest.TestCase):

    def test_len_2(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        t_start = perf_counter()
        result = strassen(A, B)
        self.assertEqual(result, expected_result)
        print("Time: %s ms" % (perf_counter() - t_start))

    def test_len_4(self):

        A = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        B = [
            [16, 15, 14, 13],
            [12, 11, 10, 9],
            [8, 7, 6, 5],
            [4, 3, 2, 1]
        ]
        expected_result = [
            [80, 70, 60, 50],
            [240, 214, 188, 162],
            [400, 358, 316, 274],
            [560, 502, 444, 386]
        ]
        result = strassen(A, B)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
