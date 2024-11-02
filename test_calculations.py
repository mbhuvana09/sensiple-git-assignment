import unittest
from addition import add
from subtraction import subtract

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=1)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2, places=1)

if __name__ == "__main__":
    unittest.main()
