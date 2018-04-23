import unittest
import challenge


class TestChallenge2(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(challenge.find_peaks([5, 10, 20, 15]),
                         (1, 2))

    def test_example_2(self):
        self.assertEqual(challenge.find_peaks([10, 20, 15, 2, 23, 90, 67]),
                         (2, 4))

    def test_check_index_is_peak_left_False(self):
        self.assertEqual(challenge.check_index_is_peak(10, 20, None),
                         False)

    def test_check_index_is_peak_left_True(self):
        self.assertEqual(challenge.check_index_is_peak(20, 10, None),
                         True)

    def test_check_index_is_peak_rigth_False(self):
        self.assertEqual(challenge.check_index_is_peak(10, None, 10),
                         False)

    def test_check_index_is_peak_rigth_True(self):
        self.assertEqual(challenge.check_index_is_peak(20, None, 10),
                         True)

    def test_check_index_is_peak_Non_Value(self):
        self.assertEqual(challenge.check_index_is_peak(20, None, None),
                         False)

    def test_check_index_is_peak_False(self):
        self.assertEqual(challenge.check_index_is_peak(20, 30, 5),
                         False)

    def test_check_index_is_peak_True(self):
        self.assertEqual(challenge.check_index_is_peak(20, 10, 5),
                         True)

if __name__ == '__main__':
    unittest.main()
