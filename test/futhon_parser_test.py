import unittest
import re
import futhon_parser


class TestFuthonParser(unittest.TestCase):

    def test_decimal(self):
        parser = futhon_parser.FuthonParser()
        self.assertEqual(15, parser.parse("15"))
        self.assertEqual(-15, parser.parse("-15"))

    def test_float(self):
        parser = futhon_parser.FuthonParser()
        self.assertEqual(15.0, parser.parse("15.0"))
        self.assertEqual(15.0, parser.parse("15."))
        self.assertEqual(-15.0, parser.parse("-15."))
        self.assertEqual(0.0, parser.parse("0.0"))

    def test_string(self):
        parser = futhon_parser.FuthonParser()
        self.assertEqual("hello", parser.parse("\"hello\""))
        self.assertEqual("", parser.parse("\"\""))

    def test_regex_string(self):
        parser = futhon_parser.FuthonParser()
        self.assertIsInstance(parser.parse("#\"\""),
                              re._pattern_type)
        self.assertIsInstance(parser.parse("#\"hello\""),
                              re._pattern_type)

    def test_boolean(self):
        parser = futhon_parser.FuthonParser()
        self.assertEqual(True, parser.parse("true"))
        self.assertEqual(False, parser.parse("false"))

    def test_keyword(self):
        parser = futhon_parser.FuthonParser()
        self.assertEqual(":key", parser.parse(":key").name)
        self.assertEqual(":key-word", parser.parse(":key-word").name)

    def test_symbol(self):
        parser = futhon_parser.FuthonParser()
        self.assertEqual("-", parser.parse("-").name)
        self.assertEqual("+", parser.parse("+").name)
        self.assertEqual("*", parser.parse("*").name)
        self.assertEqual("/", parser.parse("/").name)
        self.assertEqual("->", parser.parse("->").name)
        self.assertEqual("-0a", parser.parse("-0a").name)
        self.assertEqual("-a", parser.parse("-a").name)
        self.assertEqual("-main", parser.parse("-main").name)
        self.assertEqual("-is-symbol?", parser.parse("-is-symbol?").name)
        self.assertEqual(".some-method",
                         parser.parse(".some-method").name)

    def test_list(self):
        parser = futhon_parser.FuthonParser()
        self.assertIsInstance(parser.parse("(1 2 3)"), list)
        self.assertEqual(parser.parse("(1 2 3)"), [1, 2, 3])

    def test_hashmap(self):
        parser = futhon_parser.FuthonParser()
        self.assertIsInstance(parser.parse("{1 2 3 4}"), dict)
        self.assertEqual({1: 2, 3: 4}, parser.parse("{1 2 3 4}"))
        self.assertEqual({1: 2, 3: 4}, parser.parse("{1 2, 3 4}"))

    def test_set(self):
        parser = futhon_parser.FuthonParser()
        self.assertIsInstance(parser.parse("#{1 2 3 4}"), set)
        self.assertEqual(parser.parse("#{1 2 3 4}"), set([1, 2, 3, 4]))
        self.assertEqual(parser.parse("#{1 2 3 4 4}"), set([1, 2, 3, 4]))