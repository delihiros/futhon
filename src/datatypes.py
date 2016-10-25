class FuthonObject(object):

    def __init__(self):
        pass


class Collection(FuthonObject):

    def __init__(self):
        pass


class Sequence(Collection):

    def __init__(self):
        pass

    def next(self):
        pass


class Symbol(FuthonObject):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(self, other)


class Vector(Sequence, list):

    def __init__(self, *args, **kw):
        list.__init__(self, *args, **kw)


class Set(Collection, set):

    def __init__(self, *args, **kw):
        set.__init__(self, *args, **kw)


class HashMap(Collection, dict):

    def __init__(self, *args, **kw):
        dict.__init__(self, *args, **kw)


class Keyword(FuthonObject):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, Keyword) and self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(self, other)


class Lambda(FuthonObject):

    def __init__(self, args, body, env):
        self.args = args
        self.body = body
        self.env = env

    def __repr__(self):
        return "#<closure>"


def isFuthonObj(o):
    return isinstance(o, FuthonObject)


def isCollection(o):
    return isinstance(o, Collection)


def isSequence(o):
    return isinstance(o, Sequence)


def isVector(o):
    return isinstance(o, Vector)


def isSet(o):
    return isinstance(o, Set)


def isHashMap(o):
    return isinstance(o, HashMap)


def isSymbol(o):
    return isinstance(o, Symbol)


def isKeyword(o):
    return isinstance(o, Keyword)


def isLambda(o):
    return isinstance(o, Lambda)
