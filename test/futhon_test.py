import unittest
import futhon_parser_test
import evaluator_test


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(futhon_parser_test.TestFuthonParser))
    suite.addTests(unittest.makeSuite(evaluator_test.TestEvaluator))
    return suite
