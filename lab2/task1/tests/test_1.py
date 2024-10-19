import unittest
from time import perf_counter
import random

from lab2.task1.src.task1 import merge_sort
class TestMergeSort(unittest.TestCase):

    def test_small_list(self):
        self.small_size = 1000
        list = [random.randint(-10 ** 9, 10 ** 9) for i in range(self.small_size)]
        t_start = perf_counter()
        merge_sort(list, 0, len(list) - 1)
        self.assertEqual(list, sorted(list))
        print("Time: %s ms" %  (perf_counter() - t_start))

    def test_medium_list(self):
        self.medium_size = 10 ** 4
        list = [random.randint(-10 ** 9, 10 ** 9) for i in range(self.medium_size)]
        t_start = perf_counter()
        merge_sort(list, 0, len(list) - 1)
        self.assertEqual(list, sorted(list))
        print("Time: %s ms" % (perf_counter() - t_start))

    def test_large_list(self):
        self.large_size = 10 ** 5
        list = [random.randint(-10 ** 9, 10 ** 9) for i in range(self.large_size)]
        t_start = perf_counter()
        merge_sort(list, 0, len(list) - 1)
        self.assertEqual(list, sorted(list))
        print("Time: %s ms" % (perf_counter() - t_start))


if __name__ == '__main__':
    unittest.main()
