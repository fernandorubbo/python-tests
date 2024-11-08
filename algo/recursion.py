import unittest

def fibonacci(posi):
    if posi<=2:
        return posi
    return fibonacci(posi-1) + fibonacci(posi-2)

class TestFibonacci(unittest.TestCase):
    def test(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 2)
        self.assertEqual(fibonacci(3), 3)
        self.assertEqual(fibonacci(4), 5)
        self.assertEqual(fibonacci(5), 8)
        self.assertEqual(fibonacci(6), 13)
        self.assertEqual(fibonacci(7), 21)
        self.assertEqual(fibonacci(8), 34)

if __name__ == '__main__':
    unittest.main()
