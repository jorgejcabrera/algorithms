from unittest import TestCase

from dijkstra import dijkstra
from graph import Graph


def instance_one():
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 6, 7)
    g.add_edge(1, 6, 11)
    g.add_edge(1, 7, 20)
    g.add_edge(1, 2, 9)
    g.add_edge(2, 3, 6)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 10)
    g.add_edge(3, 5, 5)
    g.add_edge(4, 5, 15)
    g.add_edge(4, 7, 1)
    g.add_edge(4, 8, 5)
    g.add_edge(5, 8, 12)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 8, 3)
    return g


#              (5)
#       1(b) ------- 2(d)
# (4) /   |      /     | (6)\
# 0(s) (1)|  (8)/   (2)|     5(t)
# (2) \   |    /       | (2)/
#       3(c) ------- 4(e)
#             (10)
def instance_two():
    g = Graph(6)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 3, 2)
    g.add_edge(1, 2, 5)
    g.add_edge(1, 3, 1)
    g.add_edge(3, 2, 8)
    g.add_edge(3, 4, 10)
    g.add_edge(4, 2, 2)
    g.add_edge(4, 5, 2)
    g.add_edge(2, 5, 6)
    return g


class Test(TestCase):

    def test_dijkstra_instance_one(self):
        # given
        g = instance_one()

        # when
        d = dijkstra(g, 0)

        # then
        expected_result = {0: 0, 1: 4, 2: 11, 3: 17, 4: 9, 5: 22, 6: 7, 7: 8, 8: 11}
        self.assertEqual(expected_result, d)

    def test_dijkstra_instance_two(self):
        # given
        g = instance_two()

        # when
        d = dijkstra(g, 0)

        # then
        expected_result = {0: 0, 1: 3, 2: 8, 3: 2, 4: 10, 5: 12}
        self.assertEqual(expected_result, d)
