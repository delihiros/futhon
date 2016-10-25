import datatypes
import primitives


class Environment():

    def __init__(self, env, outer={}, bindings=None, args=None):
        self.env = env
        self.outer = outer
        if bindings and args:
            for bind, arg in zip(bindings, args):
                self.env[bind] = arg

    def __repr__(self):
        return str(tuple(str(self.env), str(self.outer)))

    def set(self, symbol, val):
        self.env[symbol] = val

    def get(self, symbol):
        if symbol in self.env:
            return self.env.get(symbol)
        elif self.outer:
            return self.outer.get(symbol)
        raise Exception("undefined symbol: " + symbol.name)


class GlobalEnvironment(Environment):

    def __init__(self, env, outer={}, bindings=None, args=None):
        super().__init__(env, outer={}, bindings=bindings, args=args)
        self.env = {
            datatypes.Symbol("+"): primitives._plus,
            datatypes.Symbol("-"): primitives._minus,
            datatypes.Symbol("*"): primitives._mult,
            datatypes.Symbol("/"): primitives._div,
            datatypes.Symbol("="): primitives._eq,
            datatypes.Symbol("<"): primitives._lt,
            datatypes.Symbol(">"): primitives._gt,
            datatypes.Symbol("not"): primitives._not,
            datatypes.Symbol("print"): primitives._print,
            datatypes.Symbol("read"): primitives._read,
        }
