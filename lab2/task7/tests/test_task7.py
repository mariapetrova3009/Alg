import unittest
from time import perf_counter
from lab2.task7.src.task7 import max_subarray

class TestMaxSubarray(unittest.TestCase):
    def test_worst_case(self):
        arr = [-1] * 9999 + [10000]
        expected_result = 10000

        t_start = perf_counter()
        result = max_subarray(arr)
        t_end = perf_counter()
        self.assertEqual(result, expected_result)
        print("Time: %s ms" %  (t_end - t_start))

    def test_best_case(self):
        arr = [i for i in range(1, 10001)]
        expected_result = sum(arr)

        t_start = perf_counter()
        result = max_subarray(arr)
        t_end = perf_counter()

        self.assertEqual(result, expected_result)
        print("Time: %s ms" %  (t_end - t_start))

    def test_unsorted_array(self):
        arr = [3, -2, 5, -1, 6, -3, 7, -8, 4, -10, 9, -12, 10, -13, 11, -14, 12]
        expected_result = 15
        result = max_subarray(arr)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
