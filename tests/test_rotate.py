from copy import deepcopy
import unittest

from pd_code_rotate import rotate


TREFOIL = [[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]


class RotateTests(unittest.TestCase):
    def test_rotation_is_an_involution_without_mutation(self):
        source = deepcopy(TREFOIL)
        rotated = rotate(source)
        self.assertEqual(rotate(rotated), TREFOIL)
        self.assertEqual(source, TREFOIL)

    def test_rejects_invalid_code(self):
        with self.assertRaises(ValueError):
            rotate([[1, 2, 3, 4]])


if __name__ == "__main__":
    unittest.main()
