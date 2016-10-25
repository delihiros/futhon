import unittest
import futhon_parser
import datatypes
import evaluator
import environment


class TestEvaluator(unittest.TestCase):

    def test_decimal(self):
        parser = futhon_parser.FuthonParser()
        env = environment.GlobalEnvironment({})
        ev = evaluator.Evaluator()
        self.assertEqual(15, ev.eval(parser.parse("15"), env))

    def test_vector(self):
        parser = futhon_parser.FuthonParser()
        env = environment.GlobalEnvironment({})
        ev = evaluator.Evaluator()
        self.assertEqual(datatypes.Vector([5, 4, 3]),
                         ev.eval(parser.parse("[5, 4, 3]"), env))

    def test_list(self):
        parser = futhon_parser.FuthonParser()
        env = environment.GlobalEnvironment({})
        ev = evaluator.Evaluator()
        self.assertEqual(
            "", ""
        )