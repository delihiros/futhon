import plyplus
import os
import re
import datatypes


def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False


def isint(value):
    try:
        int(value)
        return True
    except:
        return False


def iskeyword(s):
    return s.startswith(":")


class FuthonTransformer(plyplus.STransformer):

    def _start(self, node):
        return node.tail

    def _symbol(self, node):
        itm = node.tail[0]
        if itm == 'nil' or itm == 'None':
            return None
        elif itm == 'true' or itm == 'True':
            return True
        elif itm == 'false' or itm == 'False':
            return False
        elif isint(itm):
            return int(itm)
        elif isfloat(itm):
            return float(itm)
        elif iskeyword(itm):
            return datatypes.Keyword(itm)
        else:
            return datatypes.Symbol(itm)

    def _quoted(self, node):
        return [datatypes.Symbol('quote')] + node.tail

    def _string(self, node):
        return node.tail[0][1:-1]

    def _regex_string(self, node):
        return re.compile(node.tail[0][1:-1])

    def _vector(self, node):
        return datatypes.Vector(node.tail)

    def _list(self, node):
        return node.tail

    def _hashmap(self, node):
        hashmap = {}  # datatypes.HashMap()
        idx = 0
        while idx < len(node.tail):
            hashmap[node.tail[idx]] = node.tail[idx + 1]
            idx += 2
        return hashmap

    def _set(self, node):
        return datatypes.Set(node.tail)

    start = _start
    quoted = _quoted
    symbol = _symbol
    string = _string
    regex_string = _regex_string
    vector = _vector
    list = _list
    hashmap = _hashmap
    set = _set


class FuthonParser():

    def __init__(self):
        self.grammar_file = open(os.path.dirname(__file__) + "/futhon.g")
        self.grammar = plyplus.Grammar(self.grammar_file.read())
        self.grammar_file.close()
        self.transformer = FuthonTransformer()

    def parse(self, s, save=None):
        ast = self.grammar.parse(s)
        if save:
            ast.to_png_with_pydot(save)
        return self.transformer.transform(ast)[0]
