from unittest import TestCase


class TestBits_to_flip(TestCase):
    def test_bits_to_flip(self):
        try:
            from build import bits_to_flip
        except ImportError:
            self.assertFalse("No function found")

        a = int('11101', base=2)
        b = int('01111', base=2)
        expected = 2
        self.assertEqual(bits_to_flip(a, b), expected)
