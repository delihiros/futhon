import unittest
import futhon_parser_test


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(futhon_parser_test.TestFuthonParser))
    return suite