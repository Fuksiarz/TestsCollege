import unittest
from unittest import mock

from app.Kalkulator import add, subtract, divide, multiply


class kalkulator_test(unittest.TestCase):

    @mock.patch("app.Kalkulator.add")
    def test_add(self, mock_add):
        x = 7
        y = 6
        mock_add.return_value = 13
        self.assertEqual(add(x, y), mock_add.return_value)

    @mock.patch("app.Kalkulator.add")
    def test_add(self, mock_add):
        x = 7
        y = -6
        mock_add.return_value = 1
        self.assertEqual(add(x, y), mock_add.return_value)

    @mock.patch("app.Kalkulator.subtract")
    def test_sub(self, mock_sub):
        x = 7
        y = 6
        mock_sub.return_value = 1
        self.assertEqual(subtract(x, y), mock_sub.return_value)

    @mock.patch("app.Kalkulator.subtract")
    def test_sub(self, mock_sub):
        x = 7
        y = -6
        mock_sub.return_value = 13
        self.assertEqual(subtract(x, y), mock_sub.return_value)

    @mock.patch("app.Kalkulator.divide")
    def test_div(self, mock_div):
        x = 12
        y = 6
        mock_div.return_value = 2
        self.assertEqual(divide(x, y), mock_div.return_value)

    @mock.patch("app.Kalkulator.divide")
    def test_div(self, mock_div):
        x = 12
        y = -6
        mock_div.return_value = -2
        self.assertEqual(divide(x, y), mock_div.return_value)

    @mock.patch("app.Kalkulator.multiply")
    def test_mul(self, mock_mul):
        x = 10
        y = 6
        mock_mul.return_value = 60
        self.assertEqual(multiply(x, y), mock_mul.return_value)

    @mock.patch("app.Kalkulator.multiply")
    def test_mul(self, mock_mul):
        x = 10
        y = -6
        mock_mul.return_value = -60
        self.assertEqual(multiply(x, y), mock_mul.return_value)
