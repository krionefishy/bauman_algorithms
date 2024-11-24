import random
import unittest
def barrier_insertion(lst):
    barrier = 0
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        barrier += 1
        j = barrier - 1
        
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key 
    
    return lst


class Testbarrier_insertion(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(barrier_insertion(list(range(1, 101))), list(range(1, 101)))

    def test_reverse_sorted_array(self):
        self.assertEqual(barrier_insertion(list(range(100, 0, -1))), list(range(1, 101)))

    def test_empty_array(self):
        self.assertEqual(barrier_insertion([]), [])

    def test_single_element_array(self):
        self.assertEqual(barrier_insertion([42]), [42])

    def test_large_numbers(self):
        self.assertEqual(barrier_insertion([1000000000, 500, 0, -5000, 123456789, -999999999, 987654321] * 10), 
                         sorted([1000000000, 500, 0, -5000, 123456789, -999999999, 987654321] * 10))

    def test_floats(self):
        self.assertEqual(barrier_insertion([1.1, 2.2, 0.5, -1.0, 3.3, -5.5, 4.4] * 15), 
                         sorted([1.1, 2.2, 0.5, -1.0, 3.3, -5.5, 4.4] * 15))

    def test_repeated_elements(self):
        self.assertEqual(barrier_insertion([1, 1, 1, 1, 1, 1, 1, 1, 1, 1] * 10), [1] * 100)

    def test_large_dataset(self):
        
        large_list = random.sample(range(1, 10001), 5000)  # Случайная выборка из 5000 уникальных чисел
        self.assertEqual(barrier_insertion(large_list), sorted(large_list))

    def test_negative_numbers(self):
        self.assertEqual(barrier_insertion([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10] * 10), 
                         sorted([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10] * 10))

    def test_large_and_small_numbers(self):
        self.assertEqual(barrier_insertion([1, -1, 100000, -100000, 0, 500, -500] * 20), 
                         sorted([1, -1, 100000, -100000, 0, 500, -500] * 20))

if __name__ == '__main__':
    unittest.main()