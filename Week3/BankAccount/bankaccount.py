import unittest
from bank import BankAccount


class Test_BankAccount(unittest.TestCase):

    def setUp(self):
        self.rado = BankAccount("Rado", 1000, "$")
        self.ivo = BankAccount("Ivo", 0, "$")

    def test_create_account(self):
        self.assertIsInstance(self.rado, BankAccount)
        self.assertIsInstance(self.ivo, BankAccount)

    def test_deposit(self):
        with self.assertRaises(ValueError):
            self.ivo.deposit(-10)

    def test_return_balance(self):
        self.assertEqual(self.rado.amount, 1000)

    def test_withdraw_from_non_empty_account(self):
        self.rado.deposit(100)
        result = self.rado.withdraw(50)
        self.assertTrue(result)
        self.assertEqual(self.rado.balance(), 1050)

    def test_withdraw_from_empty_account(self):
        result = self.rado.withdraw(10000)
        self.assertIsNotNone(result)
        self.assertFalse(result)

    def test_string(self):
        self.assertEqual(str(self.ivo),
                         "Bank account for {} with balance of {}{}".format(
            self.ivo.name, self.ivo.amount, self.ivo.currency))

    def test_int(self):
        self.assertTrue(int(self.ivo) == 0)

    def test_transfer(self):
        self.assertTrue(self.rado.transfer_to(self.ivo, 10))

    def test_history(self):
        self.assertGreater(len(self.rado.history()), 0)

if __name__ == '__main__':
    unittest.main()
