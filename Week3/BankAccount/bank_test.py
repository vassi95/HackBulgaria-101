import unittest
from bank import BankAccount


class Test_BankAccount(unittest.TestCase):

    def setUp(self):
        self.rado = BankAccount("Rado", 1000, "$")
        self.ivo = BankAccount("Ivo", 0, "$")

    def test_init(self):
        self.assertEqual(self.rado.name, 'Rado')
        self.assertEqual(self.rado.amount, 1000)
        self.assertEqual(self.rado.currency, '$')
        self.assertEqual(self.ivo.name, 'Ivo')
        self.assertEqual(self.ivo.amount, 0)
        self.assertEqual(self.ivo.currency, '$')

    def test_str(self):
        self.rado = BankAccount("Rado", 1000, "$")
        self.assertEqual(str(self.rado),
                         "Bank account for {} with balance of {}{}".format(
                self.rado.name, self.rado.amount, self.rado.currency))
        self.ivo = BankAccount("Ivo", 0, "$")
        self.assertEqual(str(self.ivo),
                         "Bank account for {} with balance of {}{}".format(
                self.ivo.name, self.ivo.amount, self.ivo.currency))

    def test_deposit(self):
        with self.assertRaises(ValueError):
            self.ivo.deposit(-10)

    def test_balance(self):
        self.assertEqual(self.rado.amount, 1000)

    def test_withdraw(self):
        with self.assertRaises(ValueError):
            self.rado.withdraw(2000)

    def test_string(self):
        self.assertEqual(str(self.ivo),
                         "Bank account for {} with balance of {}{}".format(
            self.ivo.name, self.ivo.amount, self.ivo.currency))

    def test_int(self):
        self.assertTrue(int(self.ivo.amount) == 0)
        self.assertTrue(int(self.rado.amount) == 1000)

    def test_transfer_to(self):
        self.assertTrue(self.rado.transfer_to(self.ivo, 10))

    def test_history(self):
        self.assertGreater(len(self.rado.history()), 0)

if __name__ == '__main__':
    unittest.main()
