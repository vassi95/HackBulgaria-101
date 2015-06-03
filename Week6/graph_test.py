from graph import DirectedGraph
import unittest

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.nodes = DirectedGraph()

    def test_init(self):
        self.assertTrue(isinstance(self.nodes, DirectedGraph))

    def test_add_edge(self):
        self.nodes.add_edge("panda_1", "panda_2")
        self.nodes.add_edge("panda_1", "panda_3")
        self.assertIn("panda_1", self.nodes.nodes.keys())
        self.assertIn("panda_2", self.nodes.nodes["panda_1"])

    def test_get_neighbors_for(self):
        self.nodes.add_edge("panda_1", "panda_2")
        self.nodes.add_edge("panda_1", "panda_3")
        self.assertEqual(self.nodes.get_neighbors_for("panda_1"), ['panda_2', 'panda_3'])

    def test_path_between(self):
        self.nodes.add_edge("panda_1", "panda_2")
        self.nodes.add_edge("panda_1", "panda_3")
        self.assertTrue(self.nodes.path_between("panda_1", "panda_2"))
        self.assertTrue(self.nodes.path_between("panda_1", "panda_3"))
        self.assertFalse(self.nodes.path_between("panda_3", "panda_1"))


if __name__ == '__main__':
    unittest.main()
