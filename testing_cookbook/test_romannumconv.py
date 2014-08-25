import unittest
from romannumconv import *
class TestRomanNumeralConverter(unittest.TestCase):
    def setUp(self):
        self.cvt  = RomanNumeralConverter()

    def test_edges(self):
        r = self.cvt.convert_to_roman
        d = self.cvt.convert_to_decimal
        edges = [("equals", r, "I", 1),
                 ("equals", r, "", 0) 
                ]
        [self.checkout_edge(edge) for edge in edges]

    def test_tiers(self):
        r = self.cvt.convert_to_roman
        edges = [("equals", r, "V", 5),
                  ("equals", r, "VIIII", 9)
                ]
        [self.checkout_edge(edge) for edge in edges]

    def test_bad_inputs(self):
        r = self.cvt.convert_to_roman
        d = self.cvt.convert_to_decimal
        edges = [("equals", r, "", None),
                 ("equals", r, "I", 1.2) 
                ]
        [self.checkout_edge(edge) for edge in edges]



    def checkout_edge(self, edge):
        if edge[0] == "equals":
            f, output, input = edge[1], edge[2], edge[3]
            print("Converting %s to %s..." % (input, output))
            self.assertEquals(output, f(input))

        elif edge[0] == "raises":
            f, exception, args = edge[1], edge[2], edge[3:]
            print("Converting %s, expecting %2" % (args, exception))
            self.assertRaises(exception, f, *args)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRomanNumeralConverter)
    unittest.TextTestRunner(verbosity=2).run(suite)
