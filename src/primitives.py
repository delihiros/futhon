import sys


def _plus(args):
    s = 0
    for arg in args:
        s += arg
    return s


def _minus(args):
    if len(args) == 0:
        return 0
    s = args[0]
    for arg in args[1:]:
        s -= arg
    return s


def _div(args):
    if len(args) == 0:
        return 0
    s = args[0]
    for arg in args[1:]:
        s /= arg
    return s


def _mult(args):
    if len(args) == 0:
        return 1
    s = args[0]
    for arg in args[1:]:
        s *= arg
    return s


def _eq(args):
    if len(args) == 0:
        return True
    s = args[0]
    for arg in args[1:]:
        if s != arg:
            return False
    return True


def _lt(args):
    if len(args) == 0:
        return True
    s = args[0]
    for arg in args[1:]:
        if s >= arg:
            return False
    return True


def _gt(args):
    if len(args) == 0:
        return True
    s = args[0]
    for arg in args[1:]:
        if s <= arg:
            return False
    return True


def _not(args):
    return not args[0]


def _print(args):
    sys.stdout.write(''.join(args))


def _read(args):
    return sys.stdin.readline()