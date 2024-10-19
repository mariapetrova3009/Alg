import unittest
from time import perf_counter

from lab2.task4.src.task4 import bin

class TestBinarySearch(unittest.TestCase):

    def test_ound(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        t_start = perf_counter()
        result = bin(arr, 0, len(arr) - 1, 5)
        self.assertEqual(result, 4)
        print("Time: %s ms" % (perf_counter() - t_start))

    def test_not_found(self):
        arr = [1, 2, 3, 4, 5]
        t_start = perf_counter()
        result = bin(arr, 0, len(arr) - 1, 6)
        self.assertEqual(result, -1)
        print("Time: %s ms" % (perf_counter() - t_start))

if __name__ == '__main__':
    unittest.main()
