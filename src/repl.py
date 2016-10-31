import futhon_parser
import environment
import evaluator
import sys


class REPL():

    def __init__(self, parser, ev, global_env):
        self.parser = parser
        self.ev = ev
        self.global_env = global_env
        self.lines = ""
        self.stack = []

    def wait_or_run(self, s):
        pairs = {
            ']': '[', '}': '{', ')': '('
        }
        self.lines += s
        str_mode = False
        for c in s:
            if c == '"':
                str_mode = not str_mode
            elif not str_mode:
                if c in list(pairs.values()):
                    self.stack.append(c)
                if c in list(pairs.keys()):
                    if pairs[c] == self.stack[-1]:
                        self.stack.pop()
        if len(self.stack) == 0:
            try:
                ast = self.parser.parse(self.lines)
                self.lines = ""
                result = self.ev.eval(ast, self.global_env)
                print("# " + str(result))
                sys.stdout.write("-> ")
                sys.stdout.flush()
            except Exception as e:
                print(e)
                self.lines = ""
                sys.stdout.write("-> ")
                sys.stdout.flush()


def __main__():
    parser = futhon_parser.FuthonParser()
    ev = evaluator.Evaluator()
    global_env = environment.GlobalEnvironment({})
    repl = REPL(parser, ev, global_env)

    sys.stdout.write("-> ")
    sys.stdout.flush()
    for line in sys.stdin:
        repl.wait_or_run(line)

#    sys.stdout.write("-> ")
#    sys.stdout.flush()
#    for line in sys.stdin:
#        try:
#            ast = parser.parse(line)
#            result = ev.eval(ast, global_env)
#            print("# " + str(result))
#            sys.stdout.write("-> ")
#            sys.stdout.flush()
#        except Exception as e:
#            print(e)
#            sys.stdout.write("-> ")
#            sys.stdout.flush()

if __name__ == "__main__":
    __main__()