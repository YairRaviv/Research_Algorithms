import unittest
from Ex1 import *
import networkx as nx
from io import StringIO
import sys


class Mytes(unittest.TestCase):
    # ---------------------------------------------------Tests for Question 1-----------------------------------------
    def test1(self):
        self.assertEqual(safe_call(f1, a=1, b=2), 3)
        self.assertEqual(safe_call(f1, a=1, b=1), 2)
        self.assertEqual(safe_call(f1, a=0, b=2), 2)
        with self.assertRaises(Exception):
            safe_call(f1, a=1, b=2.0)
            safe_call(f1, a=1.1, b=0)
            safe_call(f1, a=1.2, b=0)

    def test2(self):
        self.assertEqual(safe_call(f2, a=1, b=2.0, c=0), 3.0)
        self.assertEqual(safe_call(f2, a=1, b=1.1, c=1), 3.1)
        self.assertEqual(safe_call(f2, a=0, b=2.2, c=2), 4.2)
        with self.assertRaises(Exception):
            safe_call(f2, a=1, b=2, c=0)
            safe_call(f2, a=1, b=0, c = 1)
            safe_call(f2, a=1, b=0, c = 2)

    # ---------------------------------------------------Tests for Question 2 -----------------------------------------
    def test3(self):
        g1 = nx.Graph()
        g1.add_nodes_from(range(1,11))
        g1.add_edge(1,2)
        g1.add_edge(2, 3)
        g1.add_edge(3, 4)
        g1.add_edge(4, 5)
        g1.add_edge(5, 6)
        g1.add_edge(6, 7)
        g1.add_edge(7, 8)
        g1.add_edge(8, 9)
        g1.add_edge(9, 10)
        g1.add_edge(1, 5)
        g1.add_edge(1, 2)
        self.assertEqual(breadth_first_search(1,4,g1.neighbors),[1,5,4])
        g1.add_edge(1, 4)
        self.assertEqual(breadth_first_search(1, 4, g1.neighbors), [1,4])
        self.assertEqual(breadth_first_search(1, 10, g1.neighbors), [1,5,6,7,8,9,10])


    def test4(self):
        path1 = breadth_first_search((0,0),(1,1),f3)
        self.assertTrue(path1 in [[(0,0),(0,1),(1,1)],[(0,0),(1,0),(1,1)]])
        path2 = breadth_first_search((0, 0), (2, 2), f3)
        self.assertTrue(path2 in [[(0, 0), (0, 1), (0, 2),(1,2),(2,2)],[(0, 0), (1, 0), (2, 0),(2,1),(2,2)],
                                  [(0, 0), (0, 1), (1, 1),(1,2),(2,2)],[(0, 0), (0, 1), (1, 1),(2,1),(2,2)],
                                  [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)], [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]
                                  ])

    # ---------------------------------------------------Tests for Question 3 -----------------------------------------
    def test5(self):
        buffer = StringIO()
        sys.stdout = buffer
        lst1 = [[3,2,1],[6,5,4,[8,7]]]
        print_sorted(lst1)
        out = buffer.getvalue().replace(" ","")
        self.assertEquals(out,"[[1,2,3],[4,5,6,[7,8]]]\n")


    def test6(self):
        buffer2 = StringIO()
        sys.stdout = buffer2
        lst2 = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
        print_sorted(lst2)
        out = buffer2.getvalue().replace(" ", "")
        self.assertEquals(out, "{'a':5,'b':[1,2,3,4],'c':6}\n")

def f1(a: int, b: int):
    return a + b


def f2(a: int, b: float, c:int):
    return a + b + c

def f3(node:Any)->list:
    (x,y) = node
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]



if __name__ == '__main__':
    unittest.main()
