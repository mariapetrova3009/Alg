import unittest
from time import perf_counter

from lab2.task3.src.task3 import count_inv


class TestInversionCount(unittest.TestCase):

    def test_no_inv(self):
        arr = [1, 2, 3, 4, 5]
        t_start = perf_counter()
        self.assertEqual(count_inv(arr, 0, len(arr) - 1), 0)
        print("Time: %s ms" % (perf_counter() - t_start))
    def test_inv(self):
        arr = [5, 4, 3, 2, 1]
        t_start = perf_counter()
        self.assertEqual(count_inv(arr, 0, len(arr) - 1), 10)
        print("Time: %s ms" % (perf_counter() - t_start))


if __name__ == '__main__':
    unittest.main()
