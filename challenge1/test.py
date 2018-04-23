import unittest
import challenge


class TestChallenge1(unittest.TestCase):

    def test_matrix_generation(self):
        self.assertEqual(challenge.generate_matrix(2),
                         [[[0, 0], [0, 0]], [[0, 0], [0, 0]]])

    def test_matrix_update(self):
        matrix = challenge.generate_matrix(5)
        matrix = challenge.update_matrix(matrix, [1, 1, 1], 1000)
        self.assertEqual(matrix[0][0][0], 1000)

    def test_matrix_query(self):
        matrix = challenge.generate_matrix(5)
        matrix = challenge.update_matrix(matrix, [1, 1, 1], 1000)
        matrix = challenge.update_matrix(matrix, [2, 2, 2], 1)
        matrix = challenge.update_matrix(matrix, [1, 1, 1], 5)
        matrix = challenge.update_matrix(matrix, [1, 1, 2], 4)
        matrix = challenge.update_matrix(matrix, [2, 1, 2], 1)
        matrix = challenge.update_matrix(matrix, [5, 1, 4], 10)
        total = challenge.query_matrix(matrix, [1, 1, 1, 5, 5, 5])
        self.assertEqual(total, 21)


if __name__ == '__main__':
    unittest.main()
