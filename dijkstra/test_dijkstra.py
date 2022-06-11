from unittest import TestCase

from dijkstra import dijkstra_algorithm, path_between
from graph import Graph


def instance_one():
    nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]

    init_graph = {}
    for node in nodes:
        init_graph[node] = {}

    init_graph["Reykjavik"]["Oslo"] = 5
    init_graph["Reykjavik"]["London"] = 4
    init_graph["Oslo"]["Berlin"] = 1
    init_graph["Oslo"]["Moscow"] = 3
    init_graph["Moscow"]["Belgrade"] = 5
    init_graph["Moscow"]["Athens"] = 4
    init_graph["Athens"]["Belgrade"] = 1
    init_graph["Rome"]["Berlin"] = 2
    init_graph["Rome"]["Athens"] = 2

    return Graph(nodes, init_graph)


def instance_two():
    nodes = ["s", "b", "c", "d", "e", "t"]

    init_graph = {}
    for node in nodes:
        init_graph[node] = {}

    init_graph["s"]["b"] = 4
    init_graph["s"]["c"] = 2
    init_graph["b"]["d"] = 5
    init_graph["c"]["b"] = 1
    init_graph["c"]["d"] = 8
    init_graph["c"]["e"] = 10
    init_graph["e"]["d"] = 2
    init_graph["e"]["t"] = 2
    init_graph["d"]["t"] = 6

    return Graph(nodes, init_graph)


class Test(TestCase):

    def test_dijkstra_instance_one(self):
        # given
        graph = instance_one()

        # when
        previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Reykjavik")

        # then
        expected_result = {'Reykjavik': 0, 'Oslo': 5, 'Moscow': 8, 'London': 4, 'Rome': 8, 'Berlin': 6, 'Belgrade': 11,
                           'Athens': 10}
        self.assertEqual(expected_result, shortest_path)

    def test_dijkstra_instance_two(self):
        # given
        graph = instance_two()

        # when
        previous_nodes, path_costs = dijkstra_algorithm(graph=graph, start_node="s")
        path = path_between(previous_nodes, 's', 't')

        # then
        expected_shortest_path = {'s': 0, 'b': 3, 'c': 2, 'd': 8, 'e': 10, 't': 12}
        expected_previous_nodes = {'b': 'c', 'c': 's', 'd': 'b', 'e': 'd', 't': 'e'}
        expected_path = ['s', 'c', 'b', 'd', 'e', 't']

        self.assertEqual(expected_shortest_path, path_costs)
        self.assertEqual(expected_previous_nodes, previous_nodes)
        self.assertEqual(expected_path, path)
