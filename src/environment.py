import datatypes
import primitives
import dynamic


class Environment():

    def __init__(self, env, outer={}, bindings=None, args=None):
        self.env = env
        self.outer = outer
        if bindings and args:
            if len(bindings) != len(args):
                raise Exception(
                    "environment takes same size of bindings and args.\n" +
                    "given bindings: " + str(len(bindings)) + "\n" +
                    "given args:     " + str(len(args)))
            for bind, arg in zip(bindings, args):
                self.env[bind] = arg

    def __repr__(self):
        return str(tuple(str(self.env), str(self.outer)))

    def set(self, symbol, val):
        self.env[symbol] = val

    def get(self, symbol):
        if symbol in self.env:
            return self.env.get(symbol)
        elif '.' in symbol.name:
            name_chain = symbol.name.split('.')
            v = self.env.get(datatypes.Symbol(name_chain[0]))
            return dynamic.load_class(v, name_chain[1:])
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
