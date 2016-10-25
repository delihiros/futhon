import futhon_parser
import environment
import evaluator
import sys

parser = futhon_parser.FuthonParser()
evaluator = evaluator.Evaluator()
global_env = environment.GlobalEnvironment({})


def __main__():
    sys.stdout.write("-> ")
    sys.stdout.flush()
    for line in sys.stdin:
        try:
            ast = parser.parse(line)
            result = evaluator.eval(ast, global_env)
            print("# " + str(result))
            sys.stdout.write("-> ")
            sys.stdout.flush()
        except Exception as e:
            print(e)
            sys.stdout.write("-> ")
            sys.stdout.flush()

if __name__ == "__main__":
    __main__()