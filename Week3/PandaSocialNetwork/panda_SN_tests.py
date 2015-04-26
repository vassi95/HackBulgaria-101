import unittest
from panda_social_network import Panda, PandaSocialNetwork
from panda_social_network import PandaAlreadyThere, AlreadyFriends


class TestPanda(unittest.TestCase):

    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")

    def test_init(self):
        self.assertTrue(isinstance(self.ivo, Panda))
        with self.assertRaises(TypeError):
            Panda(3, "Rado@pandamail.com", "male")
        with self.assertRaises(TypeError):
            Panda("Rado", 3, "male")
        with self.assertRaises(TypeError):
            Panda("Rado", "Rado@pandamail.com", 3)

    def test_get_name(self):
        self.assertEqual(self.ivo.get_name(), "Ivo")

    def test_get_email(self):
        self.assertEqual(self.ivo.get_email(), "ivo@pandamail.com")

    def test_get_gender(self):
        self.assertEqual(self.ivo.get_gender(), "male")

    def test_isMale(self):
        self.assertTrue(self.ivo.isMale())

    def test_isFemale(self):
        self.assertFalse(self.ivo.isFemale())

    def test_str(self):
        self.assertEqual(str(self.ivo.name), "Ivo")

    def test_eq(self):
        same_panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self. assertTrue(self.ivo == same_panda)


class TestSocialNetwork(unittest.TestCase):
    def setUp(self):
        self.net = PandaSocialNetwork()
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.rado = Panda("Rado", "rado@pandamail.com", "male")
        self.tony = Panda("Tony", "tony@pandamail.com", "female")
        for panda in [self.ivo, self.rado, self.tony]:
            self.net.add_panda(panda)

    def test_init(self):
        self.assertTrue(isinstance(self.net, PandaSocialNetwork))

    def test_add_panda(self):
        new = Panda("Dimcho", "dimcho@pandamail.com", "male")
        self.net.add_panda(new)
        with self.assertRaises(PandaAlreadyThere):
            panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.net.add_panda(panda)

    def test_make_friends(self):
        self.net.make_friends(self.ivo, self.rado)
        with self.assertRaises(AlreadyFriends):
            self.net.make_friends(self.ivo, self.rado)

    def test_friends_of(self):
        self.net.make_friends(self.ivo, self.rado)
        self.assertIn(self.rado, self.net.friends_of(self.ivo))

    def test_connection_level(self):
        self.net.make_friends(self.ivo, self.rado)
        self.net.make_friends(self.rado, self.tony)
        self.assertEqual(self.net.connection_level(self.ivo, self.rado), 1)
        self.assertEqual(self.net.connection_level(self.ivo, self.tony), 2)

    def test_are_connected(self):
        self.net.make_friends(self.ivo, self.rado)
        self.assertTrue(self.net.are_connected(self.ivo, self.rado))
        self.assertFalse(self.net.are_connected(self.ivo, self.tony))

    def test_how_many_gender_in_net(self):
        self.net.make_friends(self.ivo, self.rado)
        self.net.make_friends(self.rado, self.tony)
        toshko = Panda("Dimcho", "dimcho@pandamail.com", "male")
        self.net.make_friends(self.rado, toshko)
        self.assertEqual(self.net.how_many_gender_in_network(1, self.ivo, "male"), 1)
        self.assertEqual(self.net.how_many_gender_in_network(2, self.ivo, "female"), 0)


if __name__ == '__main__':
    unittest.main()
