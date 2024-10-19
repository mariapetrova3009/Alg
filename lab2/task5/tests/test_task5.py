import unittest
from time import perf_counter

from lab2.task5.src.task5 import majority_element
class TestMajorityElement(unittest.TestCase):
    def test_with_majority_element(self):
        arr = [2, 3, 9, 2, 2]
        t_start = perf_counter()
        result = majority_element(arr)
        self.assertEqual(result, 1)
        print("Time: %s ms" % (perf_counter() - t_start))

    def test_without_majority_element(self):
        arr = [1, 2, 3, 4]
        t_start = perf_counter()
        result = majority_element(arr)
        self.assertEqual(result, 0)
        print("Time: %s ms" % (perf_counter() - t_start))

if __name__ == '__main__':
    unittest.main()
